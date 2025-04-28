# ANNIK-A Project - Star Citizen Log Reading Discoveries (As of April 28, 2025)

## Introduction
This document summarizes all *confirmed* log reading discoveries made during the live Star Citizen log analysis and current ANNIK-A development.

## Player Identification
- **Player ID (GEID)** is assigned at login.
- Captured through two sources:
  1. **Login Event:**
     ```
     <AccountLoginCharacterStatus_Character> Character: createdAt - updatedAt - geid [PLAYER_ID] - accountId [ACCOUNT_ID] - name [PlayerName] - state STATE_CURRENT
     ```
  2. **Comms Establishment:**
     ```
     CSCCommsComponent::DoEstablishCommunicationCommon: ... for [PlayerName] [PlayerID]
     ```
- **Static PLAYER_NAME** is required in the script (case-sensitive).
- **If player ID already exists, it will not be overwritten.**

---

## Ship Spawn Events
- Ships are spawned and detected via object container streams.
- Detected by:
  ```
  EntitySpawnBatch NoNameBatch Data/objectcontainers/ships/[manufacturer]/[shipname]...
  ```
- **Only the first spawn event is captured** to prevent spamming due to multiple ship parts streaming.

---

## Hangar Platform State Tracking
- Hangar platform state transitions are clearly logged.

**Key Hangar States:**
| State | Meaning |
|:--|:--|
| LoweringPlatform | Platform lowering, preparing to store the ship |
| ClosingLoadingGate | Hangar door closing with ship inside |
| ClosedIdle | Hangar fully closed and idle, ship safely stored |
| OpeningLoadingGate | Hangar opening, preparing to retrieve ship |
| OpenIdle | Hangar open and ready for ship to leave |

- **Detection:**
  - Events tracked by matching "LoadingPlatformManager" lines.
  - Successful ship store is assumed when "ClosedIdle" happens if an active ship was previously spawned.

---

## ATC Communication Events
- Temporary communication sessions with ATC modules are logged.
- Not reliable for permanent entity tracking.
- Used to optionally confirm session activities.

---

## Force Despawn Detection (Future Expansion)
- Logs indicate server-forced ship removal:
  ```
  [net][bind]CEntity::OnOwnerRemoved: force detaching ENTITY ATTACHMENT id = ... name = "UnattendedVehicleMarker_..."
  ```
- **Not yet implemented** due to lack of clean serial number (ShipID) tracking.

---

## Internal Script Features
- `SHOW_ADDITIONAL_INFO` toggle:
  - When enabled, shows full matching raw log lines and variable changes.
- Dynamic updates printed for key variable changes:
  - `player_id`
  - `player_name`
  - `active_ship`
  - `ship_spawned`
  - `current_hangar_state`

---

## Confirmed Strategy
- Capture player ID early at login or comms.
- Track ship spawns using spawn batch entries.
- Confirm ship storing using hangar platform state "ClosedIdle".
- Record force despawn as a future feature.
- Maintain modular, expandable code design for ANNIK-A.

---

# End of Document

This documentation will be updated as ANNIK-A evolves further!