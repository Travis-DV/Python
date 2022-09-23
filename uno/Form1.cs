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
        public int[] points = { -1, -1};
        public void addcolor(string[] color, string[] number, int[] points)
        {
            this.color = color;
            this.number = number;
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
            if (type == "color") 
            {
                List<string> colors = new List<string>() {"red", "yellow", "green", "blue", "wild"};
                List<List<card>> newlist = new List<List<card>>() {new List<card>(), new List<card>(), new List<card>(), new List<card>(), new List<card>()};
                while (deck.Count > 0) { newlist[colors.IndexOf(deck[0].color[0])].Add(deck[0]); deck.RemoveAt(0);}
                foreach (List<card> l in newlist) {foreach (card c in l) {deck.Add(c);}}
            }
            else if (type == "points") 
            {
                List<card> newlist = deck;
                bool passed = false;
                while (!passed) {passed = true; for (int i = 1; i < deck.Count; i++) {if (newlist[i - 1].points[0] > newlist[i].points[0]) {passed = false; card temp = newlist[i-1]; newlist[i-1] = newlist[i]; newlist[i] = temp;}}}
            }
        }

    }

    class cardvalues
    {
        public static string[,] colors = { { "red", "yellow", "green", "blue", "red", "yellow", "green", "blue"}, { "purple", "teal", "orange", "pink", "purple", "teal", "orange", "pink" } };
        public static string[,] numbers = { { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverse", "skip" } };
        public static string[,] wilds = { { "wild", "+4", "rotate decks" } };
        public static int[,] points = { { 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 20, 25 }, {1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1 }, {30, 50, 45, -1, -1, -1, -1, -1, -1, -1, -1, -1}};
    }

    class gamelogic
    {
        List<card> deck = new List<card>();
        int startingcardnumber = 4;
        public List<player> players = new List<player>() { new player(false, "noai") };
        public gamelogic()
        {
            for (int i = 0; i < cardvalues.colors[0, 0].Length; i++) { for (int j = 0; j < 2; j++) { for (int x = j; x < 12; x++) { deck.Add(new card()); string[] newcolors = new string[] { cardvalues.colors[0, i], "" }; string[] newnumbers = { cardvalues.numbers[0, x], "" }; int[] newpoints = {cardvalues.points[0, x], -1}; deck[deck.Count-1].addcolor(newcolors, newnumbers, newpoints); } } }
            for (int i = 0; i < cardvalues.wilds[0,0].Length; i++) {card newcard = new card(); string[] color = {"wild", "wild"}; string[] number = {cardvalues.wilds[0,i], ""}; int[] pooints = {cardvalues.points[3,i], -1}newcard.addcolor();}
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
