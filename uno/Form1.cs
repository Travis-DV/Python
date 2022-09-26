﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Security.Cryptography;
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
            game.players[0].sort("color");
            game.players[1].sort("points");
            game.players[2].sort("color");
            game.players[2].sort("points");
            label1.Text = $"{game.players[0].readout("cards")}\n{game.players[1].readout("points")}\n{game.players[2].readout("cards")}\n{game.players[3].readout("cards")}";
            game.players[0].deck[0].setimage(false);
            pictureBox1 = game.players[0].deck[0].picture;
        }
    }

    class card
    {
        public string[] color = { "", "" };
        public string[] number = { "", "" };
        public int[] points = { -1, -1};
        public PictureBox picture = new PictureBox();

        public void addcolor(string[] color, string[] number, int[] points)
        {
            this.color = color;
            this.number = number;
            this.points = points;
        }

        public string getname(bool isflipped)
        {
            int i = Convert.ToInt32(isflipped);
            return $"large//{color[i]}_{number[i]}_large.png";
        }

        public void setimage(bool isflipped)
        {
            picture.Image = Image.FromFile(Application.StartupPath + "\\" + this.getname(false));
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

        public string readout(string type) 
        { 
            string word = "";
            if (type == "cards") { foreach (card c in deck) { word += $"({c.color[0]}, {c.number[0]}), "; } }
            if (type == "points") { foreach (card c in deck) { word += $"({c.points[0]}), "; } }

            return word; 
        }
        
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
                while (!passed) {passed = true; for (int i = 1; i < deck.Count; i++) {if (newlist[i - 1].points[0] < newlist[i].points[0]) {passed = false; card temp = newlist[i-1]; newlist[i-1] = newlist[i]; newlist[i] = temp;}}}
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
            for (int i = 0; i < 3; i++) {card newcard = new card(); string[] color = {"wild", "wild"}; string[] number = {cardvalues.wilds[0,i], ""}; int[] points = { cardvalues.points[2, i], -1 };  newcard.addcolor(color, number, points);}
            for (int i = 0; i < startingcardnumber - 1; i++) { players.Add(new player(true, "yesai")); }
            for (int i = 0; i < players.Count; i++) { for (int j = 0; j < 10; j++) { card addcard = deck[RandomNumber.Between(0, deck.Count)]; players[i].deck.Add(addcard); deck.Remove(addcard); } } 
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

    public static class RandomNumber
    {
        private static readonly RNGCryptoServiceProvider _generator = new RNGCryptoServiceProvider();
        public static int Between(int minimumValue, int maximumValue)
        {
            byte[] randomNumber = new byte[1];
            _generator.GetBytes(randomNumber);
            double asciiValueOfRandomCharacter = Convert.ToDouble(randomNumber[0]);
            // We are using Math.Max, and substracting 0.00000000001, 
            // to ensure "multiplier" will always be between 0.0 and .99999999999
            // Otherwise, it's possible for it to be "1", which causes problems in our rounding.
            double multiplier = Math.Max(0, (asciiValueOfRandomCharacter / 255d) - 0.00000000001d);
            // We need to add one to the range, to allow for the rounding done with Math.Floor
            int range = maximumValue - minimumValue;
            double randomValueInRange = Math.Floor(multiplier * range);
            return (int)(minimumValue + randomValueInRange);
        }
    }
}
