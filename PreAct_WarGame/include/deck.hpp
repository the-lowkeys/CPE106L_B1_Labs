/**
 * 
*/

#ifndef INCLUDE_DECK_HPP
#define INCLUDE_DECK_HPP

//Source Includes
#include "player.hpp"
#include "pile.hpp"
#include "card.hpp"

class deck
{
    //Member Variables
    pile card_deck;

    public:
        //Member Methods
        void shuffle();
        void deal_to(player player_a, player player_b);

        //Constructors
        deck();
};


#endif