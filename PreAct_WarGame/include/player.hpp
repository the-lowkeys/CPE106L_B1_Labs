/**
 * 
 * 
*/

#ifndef INCLUDE_PLAYER_HPP
#define INCLUDE_PLAYER_HPP

//Standard Library
#include <string>

//Source Headers
#include "pile.hpp"

class player
{
    //Constants
    const static int MAX_HAND_SIZE = 26;
    
    //Member Variables
    std::string player_name;

    //Player Piles
    pile play_pile;
    pile win_pile;

    //Private Methods
    void turn_over();

    public:
        //Member Methods
        player(std::string name, pile start_pile);
        
};

#endif