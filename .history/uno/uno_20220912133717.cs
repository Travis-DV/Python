#//MOVE THIS INTO .NET AT HOMEs
using system;

class card
{
    string[] name = {"", ""};
    string[] color = {"", ""};
}

class player : card {
    card[] deck;
}