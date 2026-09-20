# ConfigCore

[English](#english) · [Polski](#polski)

![Minecraft 1.21.1](https://img.shields.io/badge/Minecraft-1.21.1-62B47A)
![Fabric](https://img.shields.io/badge/Loader-Fabric-DBD0B4)
![GeckoLib](https://img.shields.io/badge/Requires-GeckoLib_4.7-2C9E8F)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## English

> A Fabric horror mod for Minecraft 1.21.1 that pretends to be an optimization library.

**Content warning:** the mod uses screen-glitch effects (red flash, flickering static bars) and disturbing themes of loss and grief. It contains no jump-scare screamers. If you are sensitive to flashing visuals, keep `safeMode` enabled (see [Configuration](#configuration)).

### What is it?

In the fiction, ConfigCore is a lightweight performance and configuration utility. In reality, it does not optimize anything. Once night falls, something starts standing in the dark and watching you.

### Features

- **Night trigger:** active from dusk to dawn (world time 13000-23000), overworld only, with no grace period.
- **Glitch Stalker:** a GeckoLib-animated entity that spawns 15-30 blocks away in dark spots (light level < 4) with a clear line of sight. It stands still, stares at you, and cannot be hurt.
- **Eye contact:** looking straight at it plays a static sound, applies short Blindness and Nausea, and glitches your screen and audio.
- **Turning away:** if you look away abruptly after eye contact, it either teleports closer or vanishes.
- **Fake console errors:** red "system" messages in chat that mention coordinates.
- **Safe mode:** one config flag disables all horror features.

### Requirements

- Minecraft **1.21.1**
- Fabric Loader 0.16+ and **Fabric API**
- **GeckoLib 4.7.x** (Fabric, 1.21.1)
- Java 21

The mod must be installed on **both the server and every client**.

### Installation

1. Install Fabric Loader for Minecraft 1.21.1.
2. Put `configcore-<version>.jar`, Fabric API and GeckoLib into your `mods` folder.
3. Start the game.

### Configuration

The config is created on first launch at `config/configcore.json`:

```json
{
  "entityCulling": true,
  "chunkCacheMb": 256,
  "adaptiveTickBudget": true,
  "safeMode": false
}
```

Only `safeMode` has an effect. Set it to `true` to disable the horror features. The other fields are part of the fiction.

### Building from source

Requires JDK 21.

```bash
git clone https://github.com/<your-username>/ConfigCore.git
cd ConfigCore
./gradlew build        # Windows: gradlew.bat build
```

The jar is written to `build/libs/configcore-<version>.jar` (do not use the `-sources` jar).

### Testing

Create a world and run `/time set 13000` to jump to night. The stalker appears within a few seconds if there is a dark spot in line of sight.

### Project structure

```
src/main/java/com/configcore/      # server + common code (entity, director, networking)
src/client/java/com/configcore/    # client-only code (renderer, stare detection, screen effects)
src/main/resources/assets/configcore/
  geo/ animations/ textures/       # GeckoLib model, animations and texture
```

### Roadmap

- [x] Night trigger, Glitch Stalker AI, eye-contact mechanics
- [x] GeckoLib model and animations
- [ ] Per-world story progress
- [ ] Text dialogues and diary log
- [ ] Cutscenes
- [ ] Multiple endings

### Credits

- Glitch Stalker model: **"THE_ENTITY" by [@nori](https://blockbenchworkshop.com/model/nori/the-entity)**, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Modified for this mod (converted to GeckoLib format, animations renamed and adjusted).
- Libraries: [Fabric API](https://github.com/FabricMC/fabric), [GeckoLib](https://github.com/bernie-g/geckolib).

### License

Code: MIT. The model is used under CC BY 4.0 (see Credits).

---

## Polski

> Horrorowy mod na Fabric dla Minecrafta 1.21.1, który udaje bibliotekę optymalizacyjną.

**Ostrzeżenie:** mod używa efektów zakłóceń ekranu (czerwony błysk, migoczące paski statyki) i porusza trudne tematy straty i żałoby. Nie ma tu krzykliwych jump scare'ów. Jeśli jesteś wrażliwy na migające obrazy, zostaw włączony `safeMode` (patrz [Konfiguracja](#konfiguracja)).

### Co to jest?

W fikcji ConfigCore to lekkie narzędzie do optymalizacji i konfiguracji. W rzeczywistości niczego nie optymalizuje. Gdy zapada noc, coś zaczyna stać w ciemności i na Ciebie patrzeć.

### Funkcje

- **Trigger nocny:** działa od zmierzchu do świtu (czas świata 13000-23000), tylko w Overworldzie, bez okresu karencji.
- **Glitch Stalker:** encja animowana w GeckoLib, która pojawia się 15-30 bloków od Ciebie w ciemnych miejscach (poziom światła < 4) z czystą linią widzenia. Stoi nieruchomo, patrzy i nie da się jej zranić.
- **Kontakt wzrokowy:** spojrzenie prosto na niego włącza dźwięk statyczny, nakłada krótką Ślepotę i Nudności oraz zakłóca ekran i dźwięk.
- **Odwrócenie się:** jeśli gwałtownie odwrócisz wzrok po kontakcie, przeteleportuje się bliżej albo zniknie.
- **Fałszywe błędy konsoli:** czerwone „systemowe" wiadomości na czacie ze współrzędnymi.
- **Tryb bezpieczny:** jedna opcja w configu wyłącza cały horror.

### Wymagania

- Minecraft **1.21.1**
- Fabric Loader 0.16+ i **Fabric API**
- **GeckoLib 4.7.x** (Fabric, 1.21.1)
- Java 21

Mod musi być zainstalowany **zarówno na serwerze, jak i u każdego gracza**.

### Instalacja

1. Zainstaluj Fabric Loader dla Minecrafta 1.21.1.
2. Wrzuć `configcore-<wersja>.jar`, Fabric API i GeckoLib do folderu `mods`.
3. Uruchom grę.

### Konfiguracja

Config powstaje przy pierwszym uruchomieniu w `config/configcore.json`:

```json
{
  "entityCulling": true,
  "chunkCacheMb": 256,
  "adaptiveTickBudget": true,
  "safeMode": false
}
```

Działa tylko `safeMode`. Ustaw `true`, żeby wyłączyć horror. Pozostałe pola są częścią fikcji.

### Budowanie ze źródeł

Wymaga JDK 21.

```bash
git clone https://github.com/<your-username>/ConfigCore.git
cd ConfigCore
./gradlew build        # Windows: gradlew.bat build
```

Jar powstaje w `build/libs/configcore-<wersja>.jar` (nie używaj pliku `-sources`).

### Testowanie

Stwórz świat i wpisz `/time set 13000`, żeby przeskoczyć do nocy. Stalker pojawi się w ciągu kilku sekund, jeśli w zasięgu wzroku jest ciemne miejsce.

### Struktura projektu

```
src/main/java/com/configcore/      # kod serwerowy i wspólny (encja, director, sieć)
src/client/java/com/configcore/    # kod tylko kliencki (renderer, wykrywanie patrzenia, efekty ekranu)
src/main/resources/assets/configcore/
  geo/ animations/ textures/       # model GeckoLib, animacje i tekstura
```

### Plan rozwoju

- [x] Trigger nocny, AI Glitch Stalkera, mechanika kontaktu wzrokowego
- [x] Model i animacje GeckoLib
- [ ] Postęp fabuły zapisywany w świecie
- [ ] Dialogi tekstowe i dziennik
- [ ] Cutscenki
- [ ] Wiele zakończeń

### Autorzy i licencje

- Model Glitch Stalkera: **„THE_ENTITY" autorstwa [@nori](https://blockbenchworkshop.com/model/nori/the-entity)**, na licencji [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Zmodyfikowany na potrzeby moda (konwersja do formatu GeckoLib, zmiana nazw i edycja animacji).
- Biblioteki: [Fabric API](https://github.com/FabricMC/fabric), [GeckoLib](https://github.com/bernie-g/geckolib).

### Licencja

Kod: MIT. Model użyty na licencji CC BY 4.0 (patrz sekcja wyżej).
