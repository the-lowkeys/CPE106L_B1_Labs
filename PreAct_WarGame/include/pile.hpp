/**
 * 
 * 
*/

#ifndef INCLUDE_PILE_HPP
#define INCLUDE_PILE_HPP

//Standard Library
#include <string>
#include <stack>

//Source Includes
#include "card.hpp"

class pile : public std::stack<card> 
{
    public:
        //Constructors
        pile();
        pile(pile& some_pile);
};

#endif