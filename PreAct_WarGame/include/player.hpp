/**
 * 
 * 
*/

#ifndef INCLUDE_PLAYER_HPP
#define INCLUDE_PLAYER_HPP

//Standard Library
#include <string>
#include <vector>

//Source Headers
#include "pile.hpp"
#include "card.hpp"

class player
{
    //Constants
    const static int MAX_HAND_SIZE = 26;
    
    //Member Variables
    std::string player_name;
    
    //Player Piles
    pile play_pile;
    pile win_pile;

    public:   

        //Member Methods
        void set_name(std::string name);
        std::string get_name();
        
        void set_play_pile(pile playing_pile);
        void add_to_win_pile(card winning_card);

        bool is_play_pile_empty();

        card peek_pop();
        std::vector<card> peek_pop(int number_of_cards);
        bool turn_over();
};

#endif