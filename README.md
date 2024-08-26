# Python-TXL24S1-C1
<h3 align="center">Flight Simulator Game</h3>
 <p align="center">
    <a href="" rel="noopener">
   <img width=325px height=220px 
    src="https://classroomclipart.com/image/content7/64941/thumb.gif" alt="Project logo"> 
    </a>
</p>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](    )
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](   )
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

# ✈️ Flight Simulator Game

## 📝 Table of Contents

- [Introduction](#introduction) 
- [Vision](#vision)
- [Functional Requirements](#functional)
- [Quality Requirements](#quality)
- [Built Using](#built)
- [Authors](#authors)
## Introduction <a name = "introduction"></a>

### 🎯 Purpose of the Document
This document outlines the requirements for the development of a flight simulator game. The primary goals of the game are to provide entertainment and educational value by allowing players to have fun while learning about sustainable development techniques. The document is intended for all stakeholders involved in the game development process, including developers, designers, project managers, and testers.

### 👥 Target Audience
The game and this document are targeted at individuals aged 12 years and older, including both the players who will engage with the game and the development team responsible for its creation.

## Vision <a name = "vision"></a>

### 💡 General Idea of the Game
The game is designed to offer players a different flying experience that merges entertainment with educational content focused on sustainable development. The primary purpose is to simulate real-world flight scenarios, allowing players to enjoy the game while learning about resource management, strategic decision-making and also learning about sustainable development.

### 🎮 Purpose of the Game
- **Entertainment**: The game encourages players to engage in logical thinking and strategy development as they attempt to escape or catch the computer-controlled opponent.
- **Education**: Players gain basic knowledge about sustainable development, particularly in the context of aviation, by managing resources and making informed decisions during gameplay.

### 🛫 Gameplay Flow
1. **Start at a Random Airport**: The game begins with the player's airplane starting from a randomly selected airport on the map.
2. **Computer Pursuit**: The computer controls another airplane, starting from a different location, and attempts to catch the player's airplane.
3. **Strategic Movement**: The player must fly to the nearest available airport on the map. Flights across continents cost more money, while flights within the same continent are less expensive.
4. **Resource Management**: Players must carefully manage their limited budget, choosing flights that maximize their chances of evading the computer or positioning themselves to catch the computer's airplane.
5. **Winning the Game**: The player wins by either escaping the computer's pursuit or catching the computer's airplane using strategic movement.

## Functional Requirements <a name = "functional"></a>

### 🛩️ User Story 1
- **Role**: As a player
- **Action**: I can select the nearest airport on the map to fly to from my current location.
- **Benefit**: So that I can make a move that aligns with the game’s rules, focusing on strategic planning to escape or catch the computer.

### 🤖 User Story 2
- **Role**: As a computer-controlled opponent
- **Action**: The computer can select the nearest airport on the map to fly to, based on its strategy to catch the player.
- **Benefit**: So that the computer follows the same rules as the player, ensuring a fair and challenging gameplay experience.

### 💰 User Story 3
- **Role**: As a player
- **Action**: I can view all nearest airports and their associated costs on the map before making a move.
- **Benefit**: So that I can make an informed decision about where to fly next, taking into consideration both the distance and cost.

### 🎁 User Story 4
- **Role**: As a player
- **Action**: I can collect props at every nearest airport I fly to.
- **Benefit**: This allows me to gain advantages such as flying twice or more in a turn, gaining extra money or special abilities that help me win the game . But at the same time some props may even have traps or penalties, such as not being able to fly for a turn.

### 🎯 User Story 5
- **Role**: As a player or computer
- **Action**: I can strategically use the props I collect during the game.
- **Benefit**: This allows me to influence the outcome of the game and increase my chances of winning by catching my opponents.

### 🏆 User Story 6
- **Role**: As a player or computer
- **Action**: I can win the game by catching the opponent's airplane by strategically moving to the nearest airports.
- **Benefit**: So that I achieve victory, ending the current game session.

### 🗺️ User Story 7
- **Role**: As a player
- **Action**:  I can view the nearest airports to my current location, flight prices and carbon footprint on a map.
- **Benefit**: This allows me to strategically plan my actions to maximise my chances of evading or catching the computer, while managing my budget.

### ⛅ User Story 8
- **Role**: As player or computer
- **Action**:  The weather can sometimes affect the departure of aircraft from the airport where they are located.
- **Benefit**: You or your opponent may be affected, while the other player will have an increased chance of catching your opponent as a result.

## Quality Requirements  <a name = "quality"></a>

### ⚡Performance Requirements
- **Map Load Time**: The map displaying the nearest airports must load within two seconds to ensure smooth gameplay.
- **Flight Selection Response Time**: The game must allow the player to select the next nearest airport within one second after the previous move is completed.

### 🖥️ Usability Requirements
- **Intuitive Interface**: The user interface must clearly display the nearest airports, the costs associated with flying to those airports, and the carbon footprint to ensure that the player understands their options at a glance.
- **Cost and Distance Clarity**: The game must visually differentiate between the costs and distances to the nearest airports to help players make strategic decisions quickly.

### 🔒 Reliability Requirements
- **Stable Gameplay**: The game must be stable, ensuring that no crashes or progress loss occurs during the gameplay. The game should have a progress save feature to save the player's progress after each move.
- **Error Handling**: If a player attempts to make an invalid move (e.g., selecting an airport that is not the nearest), the game should provide immediate feedback and prevent the action.

### 💻 Compatibility Requirements
- **Cross-Platform Compatibility**: The game should be compatible with major operating systems, including Windows, macOS, and Linux, and should support both keyboard/mouse and joystick/controller inputs.
- **Performance on Low-End Systems**: The game should run smoothly on systems that meet the minimum hardware requirements, ensuring accessibility for a wide range of users.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming
- [MariaDB](https://mariadb.org/) - Database
- [   ](    ) - Framework


## ✍️ Authors <a name = "authors"></a>

- 


