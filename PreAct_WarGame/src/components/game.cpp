/**
 * 
*/

//Standard Library
#include <iostream>
#include <fstream>
#include <filesystem>

#include <iomanip>

#include <string>
#include <vector>

//Source Headers
#include "game.hpp"
#include "deck.hpp"
#include "player.hpp"
#include "pile.hpp"
#include "card.hpp"

int player_check(player& a_player, player& b_player)
{
    //Check if either player has empty play pile
    if (a_player.is_play_pile_empty())
    {
        if (!(a_player.turn_over())) return 2;
    }
    if (b_player.is_play_pile_empty())
    {
        if (!(b_player.turn_over())) return 1;  
    }

    return 0;
};

//if equal function
int if_cards_are_equal(card a_card, card b_card, player& a_player, player& b_player)
{
    int winner;
    
    if (a_card.is_equal_to(b_card))
    {   //a == b
        unsigned int a_rank, b_rank;
        a_rank = (unsigned int) a_card.rank();
        b_rank = (unsigned int) b_card.rank();

        if (player_check(a_player, b_player) == 1) return 3;
        if (player_check(a_player, b_player) == 2) return 4;

        std::vector<card> winning_pile_a, winning_pile_b;
        winning_pile_a = a_player.peek_pop(a_rank);
        winning_pile_b = b_player.peek_pop(b_rank);
        
        int winner = if_cards_are_equal(winning_pile_a.back(), winning_pile_b.back(), a_player, b_player);
        winning_pile_a.pop_back();
        winning_pile_b.pop_back();
        if (winner == 1)
        { //a > b
            a_player.add_to_win_pile(a_card);
            a_player.add_to_win_pile(b_card);
            while (!winning_pile_a.empty())
            {
                a_player.add_to_win_pile(winning_pile_a.back());
                winning_pile_a.pop_back();
            }
            while (!winning_pile_b.empty())
            {
                a_player.add_to_win_pile(winning_pile_b.back());
                winning_pile_b.pop_back();
            }
        }

        if (winner == 2)
        { //b > a
            b_player.add_to_win_pile(a_card);
            b_player.add_to_win_pile(b_card);
            while (!winning_pile_a.empty())
            {
                b_player.add_to_win_pile(winning_pile_a.back());
                winning_pile_a.pop_back();
            }
            while (!winning_pile_b.empty())
            {
                b_player.add_to_win_pile(winning_pile_b.back());
                winning_pile_b.pop_back();
            }
        }

        return winner;
    }

    //If different
    if (a_card.is_greater_than(b_card))
    {   //a > b
        a_player.add_to_win_pile(a_card);
        a_player.add_to_win_pile(b_card);
        return 1;
    }
    else if (b_card.is_greater_than(a_card))
    {   //b > a
        b_player.add_to_win_pile(a_card);
        b_player.add_to_win_pile(b_card);
        return 2;
    }

    return winner;
};


//Essentially, the main function
game::game()
{
    //Generate the starting piles
    pile starting_pile_a, starting_pile_b;
    this->standard_deck.deal_piles(starting_pile_a, starting_pile_b);

    //Prompting Screen
    std::cout << "Game of War (by Group 5, B1)\n"
              << "Based on Ken Slonneger's Specification\n"
              << "c. 2024\n";
    
    //Get Input
    std::string temporary_input_string;
    std::filesystem::path name_file_path;
    while (true)
    {
        std::cout << "\nEnter file name/location of player names: ";
        std::cin >> std::quoted(temporary_input_string);

        //Set Into Path
        name_file_path = temporary_input_string;
        if (std::filesystem::exists(name_file_path)) break;        
        std::cout << ">>> File does not exist!!\n";
    }

    //Open File
    std::ifstream file_reader(name_file_path);
    
    //Set Names
    file_reader >> std::quoted(temporary_input_string); 
    this->player_a.set_name(temporary_input_string);
    file_reader >> std::quoted(temporary_input_string);
    this->player_b.set_name(temporary_input_string);

    //Close File
    file_reader.close();

    //Set Piles
    this->player_a.set_play_pile(starting_pile_a);
    this->player_b.set_play_pile(starting_pile_b);

    //Game Start Prompts
    std::cout << "\nCards Shuffled and Dealed. \nGame Loaded.";
    std::cout << "\nThe Players:\n" 
              << this->player_a.get_name() 
              << "\t\t\t"
              << "vs." 
              << "\t\t\t"
              << this->player_b.get_name()
              << std::endl;

    //Cards in Play
    std::vector<card> arbiter_object;
    //Lambda Print Function
    auto print_playing_cards = [](card card_a, card card_b)
    {
        std::cout << "\n";
        card_a.print_name();
        std::cout << "\t\t\tvs.\t\t\t";
        card_b.print_name();
    };

    //Game Flags
    unsigned int player_winner;

    //Actual Game
    while (true)
    {
        //Check Player Status
        if(player_check(this->player_a, this->player_b))
        {
            player_winner = player_check(this->player_a, this->player_b) - 1;
            break;
        }
        
        //Get Play Cards
        arbiter_object = {this->player_a.peek_pop(), this->player_b.peek_pop()};
        print_playing_cards(arbiter_object[0], arbiter_object[1]);

        int coded_player_winner = if_cards_are_equal(arbiter_object[0], arbiter_object[1], this->player_a, this->player_b) - 1;
        arbiter_object.clear();

        if (coded_player_winner > 2)
        {
            player_winner = coded_player_winner - 3;
            break;
        }
    }

    //Show Winner
    if (!player_winner) std::cout << "\n" << this->player_a.get_name() << "wins!";
    else std::cout << "\n>>>" << this->player_b.get_name() << " wins!";

    //Pause
    std::cin >> temporary_input_string;
}