/**
 * 
 * 
*/

#ifndef INCLUDE_CARD_HPP
#define INCLUDE_CARD_HPP

//Standard Library
#include <string>
#include <array>

class card
{
    //Public Accessible Definitions
    public:
        //Enumerations for Rank
        enum card_rank
        {
            two,
            three,
            four,
            five,
            six,
            seven,
            eight,
            nine,
            ten,
            jack,
            queen,
            king,
            ace
        };

        //Enumerations for suit
        enum card_suit
        {
            club,
            diamond,
            heart,
            spade
        };

    private:
        //Member Variables
        card_rank c_rank;
        card_suit c_suit;

        //Member Definitions
        const std::array<std::string, 13> rank_identifiers =
        {
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
            "Ace"
        };

        const std::array<std::string, 4> suit_identifier =
        {
            "Clubs",
            "Diamonds",
            "Hearts",
            "Spades"
        };
    
    public:
        //Member Methods

        // //Accessor
        void print_name();
        
        // //Rank Modifier
        card_rank rank();
        bool rank(card_rank set_rank);

        // //Suit Modifier
        card_suit suit();
        bool suit(card_suit set_suit);

        // //Comparators
        bool is_equal_to(card other_card);
        bool is_greater_than(card other_card);
        
        // //Constructors
        card(card_rank some_rank, card_suit some_suit);
};      
#endif 