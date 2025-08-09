### Todo

- [ ] better visual division of 4 sections in the settings menu
- [ ] Implement a simulation timing mode where, if the system lags, the simulation simply slows down instead of skipping simulation steps. This ensures that every simulation step is processed in order, allowing for later speed-up, and avoids the current behavior where frame updates are tied to real system time and steps may be skipped.

### Done ✓

- [x] Toggle option for frame counter
- [x] Add frame counter
- [x] Add fullscreen mode that can be toggled by button click
- [x] Many of the colormaps do not work with the function design, they have to be filtered out
- [x] Refactored the config file to include more hardcoded selections