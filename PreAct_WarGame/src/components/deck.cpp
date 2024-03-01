/**
 * 
*/

//Standard Library
#include <chrono>

//Source Includes
#include "deck.hpp"
#include "pile.hpp"
#include "card.hpp"


void deck::deal_piles(pile player_a_pile, pile player_b_pile)
{
    while (!(this->card_deck.empty()))
    {
        //Give piles to both players
        player_a_pile.push(this->card_deck.top());
        card_deck.pop();
        player_b_pile.push(this->card_deck.top());
        card_deck.pop();
    }
}

//The constructor is already preshuffled
deck::deck()
{
    //Create all Possible Cards in Deck, all while shuffling.
    std::srand(std::chrono::system_clock::now().time_since_epoch().count());
    while (this->card_deck.size() != deck::MAX_DECK_SIZE)
    {
        unsigned int random_rank = std::rand() % 13;
        unsigned int random_suit = std::rand() % 4;

        //create card, and compare if it already exists.
        card new_card((card::card_rank) random_rank, (card::card_suit) random_suit);
        pile deck_cards = this->card_deck;
        bool card_already_exists = false;
        while (!deck_cards.empty())
        {
            if (deck_cards.top().is_equal_to(new_card))
            {
                card_already_exists = true; 
                break;
            }
            //if it isn't the same, then pop from the check pile and continue
            deck_cards.pop();
        }
        //Add to card_deck if card doesn't exist yet.
        if (!card_already_exists) this->card_deck.push(new_card);
    }   
}