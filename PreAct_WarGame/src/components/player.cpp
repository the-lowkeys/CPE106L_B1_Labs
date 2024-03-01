/**
 * 
*/

//Standard Library
#include <string>

//Source Headers
#include "player.hpp"
#include "pile.hpp"
#include "card.hpp"

void player::set_name(std::string name)
{
    this->player_name = name;
}

std::string player::get_name()
{
    return this->player_name;
}

void player::set_play_pile(pile playing_pile)
{
    this->play_pile = playing_pile;
}

void player::add_to_win_pile(card winning_card)
{
    this->win_pile.push(winning_card);
}

bool player::is_play_pile_empty()
{
    if (this->play_pile.empty()) return true;
    return false;
}

card player::peek_pop()
{
    card get_card = this->play_pile.top();
    this->play_pile.pop();

    return get_card;
}

std::vector<card> player::peek_pop(int number_of_cards)
{
    std::vector<card> peeking_hand;
    for (number_of_cards; number_of_cards > 0; number_of_cards--)
    {
        peeking_hand.push_back(this->play_pile.top());
        this->play_pile.pop();
    }

    return peeking_hand;
}

/**
 * turn_over(), returns true if successfully turns over, if not, false.
*/
bool player::turn_over()
{
    if (this->win_pile.empty() || !(this->play_pile.empty())) return false;
    
    //Send the win pile to the play pile
    while (!(this->win_pile.empty()))
    {
        this->play_pile.push(win_pile.top());
        this->win_pile.pop();
    }

    return true;
}






