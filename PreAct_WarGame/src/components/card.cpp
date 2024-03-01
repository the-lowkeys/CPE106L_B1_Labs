//Standard Library
#include <iostream>

#include <string>
#include <array>

//Source Headers
#include "card.hpp"

//Card Member Methods Implmentation

// //Accessor
void card::print_name()
{
    std::cout << card::rank_identifiers.at(this->c_rank) + " of " + card::suit_identifier.at(this->c_suit);
}

// //Rank Modifiers
card::card_rank card::rank()
{
    return this->card::c_rank;
}

bool card::rank(card::card_rank set_rank)
{
    if (this->card::c_rank == set_rank) return false;
    card::c_rank = set_rank;
    return true;
}

// //Suit Modifiers
card::card_suit card::suit()
{
    return this->card::c_suit;
}

bool card::suit(card::card_suit set_suit)
{
    if (this->card::c_suit == set_suit) return false;
    card::c_suit = set_suit;
    return true;
}

// //Comparators
bool card::is_equal_to(card other_card)
{
    //Check if the same object, then rank
    if (this->c_rank == other_card.c_rank) return true;
    return false;
}

bool card::is_greater_than(card other_card)
{
    //Compare rank and suit
    if (this->c_rank > other_card.c_rank) return true;
    return false;
}

// //Constructors
card::card(card_rank some_rank, card_suit some_suit)
{
    this->card::c_rank = some_rank;
    this->card::c_suit = some_suit;
}

