# ConfigCore (Fabric 1.21.1) v1.1.0

## Budowanie (JDK 21 + internet)

    Windows:      gradlew.bat build
    Linux / Mac:  ./gradlew build

Jar: `build/libs/configcore-1.1.0.jar` (NIE bierz `-sources.jar`).
Do folderu `mods` wrzuć: ten jar + **Fabric API 1.21.1** + **GeckoLib 4.7.x dla 1.21.1** (fabric).

## Model (GeckoLib)
- `assets/configcore/geo/entity/glitch_stalker.geo.json`
- `assets/configcore/animations/entity/glitch_stalker.animation.json`
  (idle, walk, chaos, aura; `chaos` odpala się przy kontakcie wzrokowym)
- `assets/configcore/textures/entity/glitch_stalker.png`
Skala renderu 0.6 w `GlitchStalkerRenderer`, hitbox 0.6 x 2.6 w `ModEntities`.

## Głosy
Wrzuć nagrania (mono .ogg) do `src/main/resources/assets/configcore/sounds/voice/`
jako `daniel_01.ogg`..`daniel_11.ogg` i `milo_01.ogg`..`milo_15.ogg`, potem:

    python tools/gen_sounds.py

i zbuduj mod ponownie.

## Test
`/time set 13000`. Wyłączenie horroru: `"safeMode": true` w `config/configcore.json`.

## Credits
Model "THE_ENTITY" by nori (https://blockbenchworkshop.com/model/nori/the-entity), CC BY 4.0. Zmodyfikowany na potrzeby moda.
