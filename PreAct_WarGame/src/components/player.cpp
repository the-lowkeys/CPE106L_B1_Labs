/**
 * 
*/

//Standard Library
#include <string>

//Source Headers
#include "player.hpp"
#include "pile.hpp"

void player::turn_over()
{
    if (this->play_pile.empty())
    {
        this->play_pile.swap(this->win_pile);
    }
}






