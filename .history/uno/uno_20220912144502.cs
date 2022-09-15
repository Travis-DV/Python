#//MOVE THIS INTO .NET AT HOMEs
using system;

class card
{
    private string[] color = {"", ""};
    private string[] number = {"", ""};

    public void addcolor(string[] color, string[] number){
        
    }
}

class player : card {
    private card[] deck;

    public void player() {}

}

class cardvalues{
    string[,] colors = {{"red", "yellow", "green", "blue", "red", "yellow", "green", "blue", "wild"}, {"purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "wild"}};
    string[,] numbers = {{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverse", "skip"}};
    string[,] wilds = {{"wild", "+4", "rotate decks"}};
    int[,] pointsnumbers = {1,2,3,4,5,6,7,8,9,12,20,25};
}

class gamelogic {

    card[] deck;
    int startingcardnumber;
    
    public void gamelogic() {
        for (int i = 0; i < 8; i++) {card()}
    }
}