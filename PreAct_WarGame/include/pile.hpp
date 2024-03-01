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

//Yes. This is literally our definition for pile.
class pile : public std::stack<card> {};

#endif