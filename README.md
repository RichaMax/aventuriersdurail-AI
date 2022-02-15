# aventuriersdurail-AI

taken from: https://www.jeuxavolonte.asso.fr/regles/les_aventuriers_du_rail.pdf

# Goal of the project

Create an IA algorithm capable of playing Les aventuries du rail (US) boardgame 


# The game

From 2 to 5 players (red, blue, green, yellow, black) - 45 wagons each

The **wagon deck** is composed of 110 cards:
  - 12 of each types (pink, white, blue, yellow, orange, black, red, green)
  - 14 locomotives (joker can be any color)
 
The **destination deck** is composed of 30 destinatiosn cards which correspond to 2 cities that you should link. Each desination is worth a certain amount of points.

## Goal of the game

Score the highest number of points by
  - Capturing road between cities
  - Linking two cities with a continuous road (from your destinations cards)
  - Creating the longest road of train
  - If a player does not complete his destination he loses the points of the cards

## Game preparation

- Each player is given 4 wagons cards from the deck 
- Each player is given 3 destinations cards and must keep at least 2 of them (only at the begining)
- Draw 5 wagons card for the wagon deck face up. If at any time in the game there is 3 locomotives cards among the 5 cards face up the cards are discarded and five new are drawn.

## Rules

Possible action (one per turn)
- Draw 2 wagons cards (or one locomotive)for the face up car, when one take a card from the face up one, the card at the top of the facedown deck is revealed
- Draw 2 cards directly from the top of the face down deck
- Draw three destination card and selected at least one
- put train on a road

To put a train on a road the player needs to play a series of card of the color and length of the road we want to create and the cards are discarded.

The neutral connection can be made by any color as long as you have the correct amount of cards.

For the cities connected by double road, in the 2 or 3 players configuration, only one of them can be used
