/**
 * 
*/

#ifndef INCLUDE_DECK_HPP
#define INCLUDE_DECK_HPP

//Source Includes
#include "pile.hpp"
#include "card.hpp"

class deck
{
    //Constants
    const static int MAX_DECK_SIZE = 52;

    //Member Variables
    pile card_deck;

    public:
        //Member Methods
        void deal_piles(pile& player_a_pile, pile& player_b_pile);

        //Constructors
        deck();
};


#endif