# Palembang Weather Forecast 🌤️

A simple browser extension that displays the current weather and forecast for Palembang, Indonesia.

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Development](#development)  
- [License](#license)  

---

## About

This extension fetches live weather data for Palembang using a public weather API and presents it in a clean, accessible interface directly in your browser toolbar.

---

## Features

- Real-time weather: temperature, humidity, wind, and conditions   
- Refresh button to manually update data  
- Lightweight and easy-to-use popup interface  

---

## Installation

### Load as Unpacked Extension

1. Clone the repo:
   ```bash
   git clone https://github.com/randy-ariesta-muliawan/PalembangWeatherForecast.git
   cd PalembangWeatherForecast
2. Open chrome://extensions/ in Chrome.
3. Enable Developer mode (toggle in top-right).
4. Click Load unpacked and select the project folder.

5. The extension icon should appear in your toolbar.

## Usage
1. Click the extension icon.
2. View current weather and forecast for Palembang.
3. Click the Refresh button to update data manually — it also auto-refreshes every hour.

## Configuration
By default, the extension targets Palembang weather. If you'd like to adapt it:
1. Open main.py
2. Replace with your desired location's API ID or coordinates.
3. Rebuild and reload the extension.
