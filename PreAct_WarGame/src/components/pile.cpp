/**
 * 
*/

//Standard Library
#include <string>
#include <stack>

//Source Includes
#include "card.hpp"
#include "pile.hpp"

//Constructor Definition
pile::pile() {}

pile::pile(pile& some_pile)
{
    *this = some_pile;
}