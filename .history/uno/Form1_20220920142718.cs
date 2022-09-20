using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace uno
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            gamelogic game = new gamelogic();
            label1.Text = $"{game.players[0].readoutcards()}\n{game.players[1].readoutcards()}\n{game.players[2].readoutcards()}\n{game.players[3].readoutcards()}";
        }
    }

   class card
    {
        public string[] color = { "", "" };
        public string[] number = { "", "" };
        public void addcolor(string[] newcolor, string[] newnumber)
        {
            color = newcolor;
            number = newnumber;
        }
    }

    class player
    {
        public List<card> deck = new List<card>();
        public bool aicontroled;
        public string name;
        public player(bool aicontroled, string name)
        {
            this.aicontroled = aicontroled;
            this.name = name;
        }

        public string readoutcards() { string word = ""; foreach (card c in deck) { word += $"({c.color[0]}, {c.number[0]}), "; } return word; }
        
        public void sort(string type) 
        {
            List<card> newlist = new List<card>();
            if (type == "color") 
            {
                List<string> currentcolor = new List<string>() {"red", "yellow", "green", "blue", "wild"};
                while (deck.Count > 0) {foreach (card c in deck) {bool passed = true; if (c.color[0] == currentcolor[0]) {passed = false; newlist.Add(c); deck.Remove(c);} if (passed) {currentcolor.Remove(currentcolor[0]);}}}
            }
            else if (type == "points") {}
        }

    }

    class cardvalues
    {
        public static string[,] colors = { { "red", "yellow", "green", "blue", "red", "yellow", "green", "blue", "wild" }, { "purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink", "wild" } };
        public static string[,] numbers = { { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverse", "skip" } };
        public static string[,] wilds = { { "wild", "+4", "rotate decks" } };
        public static int[,] pointsnumbers = { { 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 20, 25 } };
    }

    class gamelogic
    {
        List<card> deck = new List<card>();
        int startingcardnumber = 4;
        public List<player> players = new List<player>() { new player(false, "noai") };
        public gamelogic()
        {
            for (int i = 0; i < cardvalues.colors[0, 0].Length; i++) { for (int j = 0; j < 2; j++) { for (int x = j; x < 12; x++) { deck.Add(new card()); string[] newcolors = new string[] { cardvalues.colors[0, i], "" }; string[] newnumbers = { cardvalues.numbers[0, x], "" }; deck[deck.Count - 1].addcolor(newcolors, newnumbers); } } }
            for (int i = 0; i < startingcardnumber - 1; i++) { players.Add(new player(true, "yesai")); }
            for (int i = 0; i < players.Count; i++) { for (int j = 0; j < 10; j++) { Random rnd = new Random(); card addcard = deck[rnd.Next(deck.Count)]; players[i].deck.Add(addcard); this.deck.Remove(addcard); } } 
        }
        
        private List<card>  drawtomatch(player pl, string[] color, bool fliped) 
        {
            Random rnd = new Random();
            card newcard = new card();
            List<card> addlist = new List<card>();
            while ((!fliped && newcard.color[0] != color[0]) || (fliped && newcard.color[1] != color[1])) 
            {
                addlist.Add(newcard);
                newcard = deck[rnd.Next(deck.Count)];
            }
            return addlist;
        }
    }
}
