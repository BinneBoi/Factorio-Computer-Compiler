# Contains the json that will be used for the combinators

everythingCombinator = """
{
  "blueprint": {
    "icons": [
      {
        "signal": {
          "name": "constant-combinator"
        },
        "index": 1
      }
    ],
    "entities": [
      {
        "entity_number": 1,
        "name": "constant-combinator",
        "position": {
          "x": 562.5,
          "y": -24.5
        },
        "direction": 4,
        "control_behavior": {
          "sections": {
            "sections": [
              {
                "index": 1,
                "filters": [
                  {
                    "index": 1,
                    "type": "virtual",
                    "name": "signal-deny",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 4194304
                  },
                  {
                    "index": 2,
                    "type": "virtual",
                    "name": "signal-0",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 8388608
                  },
                  {
                    "index": 3,
                    "type": "virtual",
                    "name": "signal-1",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 12582912
                  },
                  {
                    "index": 4,
                    "type": "virtual",
                    "name": "signal-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 16777216
                  },
                  {
                    "index": 5,
                    "type": "virtual",
                    "name": "signal-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 20971520
                  },
                  {
                    "index": 6,
                    "type": "virtual",
                    "name": "signal-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 25165824
                  },
                  {
                    "index": 7,
                    "type": "virtual",
                    "name": "signal-5",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 29360128
                  },
                  {
                    "index": 8,
                    "type": "virtual",
                    "name": "signal-6",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 33554432
                  },
                  {
                    "index": 9,
                    "type": "virtual",
                    "name": "signal-7",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 37748736
                  },
                  {
                    "index": 10,
                    "type": "virtual",
                    "name": "signal-8",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 41943040
                  },
                  {
                    "index": 11,
                    "type": "virtual",
                    "name": "signal-9",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 46137344
                  },
                  {
                    "index": 12,
                    "type": "virtual",
                    "name": "signal-dot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 50331648
                  },
                  {
                    "index": 13,
                    "type": "virtual",
                    "name": "shape-circle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 54525952
                  },
                  {
                    "index": 14,
                    "type": "virtual",
                    "name": "signal-clock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 58720256
                  },
                  {
                    "index": 15,
                    "type": "virtual",
                    "name": "signal-battery-low",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 62914560
                  },
                  {
                    "index": 16,
                    "type": "virtual",
                    "name": "signal-battery-mid-level",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 67108864
                  },
                  {
                    "index": 17,
                    "type": "virtual",
                    "name": "signal-battery-full",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 71303168
                  },
                  {
                    "index": 18,
                    "type": "virtual",
                    "name": "signal-clockwise-circle-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 75497472
                  },
                  {
                    "index": 19,
                    "type": "virtual",
                    "name": "signal-recycle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 79691776
                  },
                  {
                    "index": 20,
                    "type": "virtual",
                    "name": "signal-shuffle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 83886080
                  },
                  {
                    "index": 21,
                    "type": "virtual",
                    "name": "signal-stack-size",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 88080384
                  },
                  {
                    "index": 22,
                    "name": "burner-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 92274688
                  },
                  {
                    "index": 23,
                    "name": "inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 96468992
                  },
                  {
                    "index": 24,
                    "name": "long-handed-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 100663296
                  },
                  {
                    "index": 25,
                    "name": "fast-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 104857600
                  },
                  {
                    "index": 26,
                    "name": "bulk-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 109051904
                  },
                  {
                    "index": 27,
                    "name": "transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 113246208
                  },
                  {
                    "index": 28,
                    "name": "fast-transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 117440512
                  },
                  {
                    "index": 29,
                    "name": "express-transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 121634816
                  },
                  {
                    "index": 30,
                    "name": "locomotive",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 125829120
                  },
                  {
                    "index": 31,
                    "name": "cargo-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 130023424
                  },
                  {
                    "index": 32,
                    "name": "fluid-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 134217728
                  },
                  {
                    "index": 33,
                    "name": "artillery-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 138412032
                  },
                  {
                    "index": 34,
                    "name": "car",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 142606336
                  },
                  {
                    "index": 35,
                    "name": "tank",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 146800640
                  },
                  {
                    "index": 36,
                    "name": "spidertron",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 150994944
                  },
                  {
                    "index": 37,
                    "name": "underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 155189248
                  },
                  {
                    "index": 38,
                    "name": "construction-robot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 159383552
                  },
                  {
                    "index": 39,
                    "name": "active-provider-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 163577856
                  },
                  {
                    "index": 40,
                    "name": "passive-provider-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 167772160
                  },
                  {
                    "index": 41,
                    "name": "small-lamp",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 171966464
                  },
                  {
                    "index": 42,
                    "name": "arithmetic-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 176160768
                  },
                  {
                    "index": 43,
                    "name": "fast-splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 180355072
                  },
                  {
                    "index": 44,
                    "name": "selector-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 184549376
                  },
                  {
                    "index": 45,
                    "name": "storage-tank",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 188743680
                  },
                  {
                    "index": 46,
                    "name": "pump",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 192937984
                  },
                  {
                    "index": 47,
                    "name": "programmable-speaker",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 197132288
                  },
                  {
                    "index": 48,
                    "name": "display-panel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 201326592
                  },
                  {
                    "index": 49,
                    "name": "stone-brick",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 205520896
                  },
                  {
                    "index": 50,
                    "name": "concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 209715200
                  },
                  {
                    "index": 51,
                    "name": "hazard-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 213909504
                  },
                  {
                    "index": 52,
                    "name": "refined-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 218103808
                  },
                  {
                    "index": 53,
                    "name": "refined-hazard-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 222298112
                  },
                  {
                    "index": 54,
                    "name": "landfill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 226492416
                  },
                  {
                    "index": 55,
                    "name": "cliff-explosives",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 230686720
                  },
                  {
                    "index": 56,
                    "name": "repair-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 234881024
                  },
                  {
                    "index": 57,
                    "name": "blueprint",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 239075328
                  },
                  {
                    "index": 58,
                    "name": "deconstruction-planner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 243269632
                  },
                  {
                    "index": 59,
                    "name": "upgrade-planner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 247463936
                  },
                  {
                    "index": 60,
                    "name": "blueprint-book",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 251658240
                  },
                  {
                    "index": 61,
                    "name": "boiler",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 255852544
                  },
                  {
                    "index": 62,
                    "name": "steam-engine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 260046848
                  },
                  {
                    "index": 63,
                    "name": "solar-panel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 264241152
                  },
                  {
                    "index": 64,
                    "name": "accumulator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 268435456
                  },
                  {
                    "index": 65,
                    "name": "nuclear-reactor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 272629760
                  },
                  {
                    "index": 66,
                    "name": "express-underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 276824064
                  },
                  {
                    "index": 67,
                    "name": "heat-exchanger",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 281018368
                  },
                  {
                    "index": 68,
                    "name": "steam-turbine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 285212672
                  },
                  {
                    "index": 69,
                    "name": "burner-mining-drill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 289406976
                  },
                  {
                    "index": 70,
                    "name": "electric-mining-drill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 293601280
                  },
                  {
                    "index": 71,
                    "name": "offshore-pump",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 297795584
                  },
                  {
                    "index": 72,
                    "name": "pumpjack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 301989888
                  },
                  {
                    "index": 73,
                    "name": "stone-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 306184192
                  },
                  {
                    "index": 74,
                    "name": "steel-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 310378496
                  },
                  {
                    "index": 75,
                    "name": "electric-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 314572800
                  },
                  {
                    "index": 76,
                    "name": "fast-underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 318767104
                  },
                  {
                    "index": 77,
                    "name": "assembling-machine-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 322961408
                  },
                  {
                    "index": 78,
                    "name": "assembling-machine-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 327155712
                  },
                  {
                    "index": 79,
                    "name": "oil-refinery",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 331350016
                  },
                  {
                    "index": 80,
                    "name": "chemical-plant",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 335544320
                  },
                  {
                    "index": 81,
                    "name": "centrifuge",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 339738624
                  },
                  {
                    "index": 82,
                    "name": "lab",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 343932928
                  },
                  {
                    "index": 83,
                    "name": "wooden-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 348127232
                  },
                  {
                    "index": 84,
                    "name": "speed-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 352321536
                  },
                  {
                    "index": 85,
                    "name": "speed-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 356515840
                  },
                  {
                    "index": 86,
                    "name": "speed-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 360710144
                  },
                  {
                    "index": 87,
                    "name": "efficiency-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 364904448
                  },
                  {
                    "index": 88,
                    "name": "efficiency-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 369098752
                  },
                  {
                    "index": 89,
                    "name": "efficiency-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 373293056
                  },
                  {
                    "index": 90,
                    "name": "productivity-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 377487360
                  },
                  {
                    "index": 91,
                    "name": "productivity-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 381681664
                  },
                  {
                    "index": 92,
                    "name": "productivity-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 385875968
                  },
                  {
                    "index": 93,
                    "name": "rocket-silo",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 390070272
                  },
                  {
                    "index": 94,
                    "name": "cargo-landing-pad",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 394264576
                  },
                  {
                    "index": 95,
                    "name": "steel-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 398458880
                  },
                  {
                    "index": 96,
                    "type": "recipe",
                    "name": "basic-oil-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 402653184
                  },
                  {
                    "index": 97,
                    "name": "logistic-robot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 406847488
                  },
                  {
                    "index": 98,
                    "type": "recipe",
                    "name": "coal-liquefaction",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 411041792
                  },
                  {
                    "index": 99,
                    "type": "recipe",
                    "name": "heavy-oil-cracking",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 415236096
                  },
                  {
                    "index": 100,
                    "type": "recipe",
                    "name": "light-oil-cracking",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 419430400
                  },
                  {
                    "index": 101,
                    "type": "recipe",
                    "name": "solid-fuel-from-petroleum-gas",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 423624704
                  },
                  {
                    "index": 102,
                    "type": "recipe",
                    "name": "solid-fuel-from-light-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 427819008
                  },
                  {
                    "index": 103,
                    "type": "recipe",
                    "name": "solid-fuel-from-heavy-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 432013312
                  },
                  {
                    "index": 104,
                    "name": "express-splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 436207616
                  },
                  {
                    "index": 105,
                    "name": "coal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 440401920
                  },
                  {
                    "index": 106,
                    "name": "stone",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 444596224
                  },
                  {
                    "index": 107,
                    "name": "iron-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 448790528
                  },
                  {
                    "index": 108,
                    "name": "copper-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 452984832
                  },
                  {
                    "index": 109,
                    "name": "uranium-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 457179136
                  },
                  {
                    "index": 110,
                    "name": "raw-fish",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 461373440
                  },
                  {
                    "index": 111,
                    "name": "iron-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 465567744
                  },
                  {
                    "index": 112,
                    "name": "copper-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 469762048
                  },
                  {
                    "index": 113,
                    "name": "steel-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 473956352
                  },
                  {
                    "index": 114,
                    "name": "solid-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 478150656
                  },
                  {
                    "index": 115,
                    "name": "plastic-bar",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 482344960
                  },
                  {
                    "index": 116,
                    "name": "sulfur",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 486539264
                  },
                  {
                    "index": 117,
                    "name": "battery",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 490733568
                  },
                  {
                    "index": 118,
                    "name": "explosives",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 494927872
                  },
                  {
                    "index": 119,
                    "name": "water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 499122176
                  },
                  {
                    "index": 120,
                    "name": "crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 503316480
                  },
                  {
                    "index": 121,
                    "name": "petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 507510784
                  },
                  {
                    "index": 122,
                    "name": "light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 511705088
                  },
                  {
                    "index": 123,
                    "name": "decider-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 515899392
                  },
                  {
                    "index": 124,
                    "name": "lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 520093696
                  },
                  {
                    "index": 125,
                    "name": "sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 524288000
                  },
                  {
                    "index": 126,
                    "name": "power-switch",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 528482304
                  },
                  {
                    "index": 127,
                    "type": "recipe",
                    "name": "crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 532676608
                  },
                  {
                    "index": 128,
                    "type": "recipe",
                    "name": "petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 536870912
                  },
                  {
                    "index": 129,
                    "type": "recipe",
                    "name": "light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 541065216
                  },
                  {
                    "index": 130,
                    "type": "recipe",
                    "name": "heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 545259520
                  },
                  {
                    "index": 131,
                    "type": "recipe",
                    "name": "lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 549453824
                  },
                  {
                    "index": 132,
                    "type": "recipe",
                    "name": "sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 553648128
                  },
                  {
                    "index": 133,
                    "type": "recipe",
                    "name": "empty-water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 557842432
                  },
                  {
                    "index": 134,
                    "type": "recipe",
                    "name": "empty-crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 562036736
                  },
                  {
                    "index": 135,
                    "type": "recipe",
                    "name": "empty-petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 566231040
                  },
                  {
                    "index": 136,
                    "type": "recipe",
                    "name": "empty-light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 570425344
                  },
                  {
                    "index": 137,
                    "type": "recipe",
                    "name": "empty-heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 574619648
                  },
                  {
                    "index": 138,
                    "type": "recipe",
                    "name": "empty-lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 578813952
                  },
                  {
                    "index": 139,
                    "type": "recipe",
                    "name": "empty-sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 583008256
                  },
                  {
                    "index": 140,
                    "name": "iron-gear-wheel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 587202560
                  },
                  {
                    "index": 141,
                    "name": "iron-stick",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 591396864
                  },
                  {
                    "index": 142,
                    "name": "copper-cable",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 595591168
                  },
                  {
                    "index": 143,
                    "name": "barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 599785472
                  },
                  {
                    "index": 144,
                    "name": "constant-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 603979776
                  },
                  {
                    "index": 145,
                    "name": "advanced-circuit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 608174080
                  },
                  {
                    "index": 146,
                    "name": "processing-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 612368384
                  },
                  {
                    "index": 147,
                    "name": "engine-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 616562688
                  },
                  {
                    "index": 148,
                    "name": "electric-engine-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 620756992
                  },
                  {
                    "index": 149,
                    "name": "flying-robot-frame",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 624951296
                  },
                  {
                    "index": 150,
                    "name": "low-density-structure",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 629145600
                  },
                  {
                    "index": 151,
                    "name": "rocket-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 633339904
                  },
                  {
                    "index": 152,
                    "type": "recipe",
                    "name": "rocket-part",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 637534208
                  },
                  {
                    "index": 153,
                    "type": "recipe",
                    "name": "uranium-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 641728512
                  },
                  {
                    "index": 154,
                    "name": "uranium-235",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 645922816
                  },
                  {
                    "index": 155,
                    "name": "uranium-238",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 650117120
                  },
                  {
                    "index": 156,
                    "name": "uranium-fuel-cell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 654311424
                  },
                  {
                    "index": 157,
                    "name": "depleted-uranium-fuel-cell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 658505728
                  },
                  {
                    "index": 158,
                    "type": "recipe",
                    "name": "nuclear-fuel-reprocessing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 662700032
                  },
                  {
                    "index": 159,
                    "type": "recipe",
                    "name": "kovarex-enrichment-process",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 666894336
                  },
                  {
                    "index": 160,
                    "name": "nuclear-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 671088640
                  },
                  {
                    "index": 161,
                    "name": "automation-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 675282944
                  },
                  {
                    "index": 162,
                    "name": "logistic-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 679477248
                  },
                  {
                    "index": 163,
                    "name": "military-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 683671552
                  },
                  {
                    "index": 164,
                    "name": "beacon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 687865856
                  },
                  {
                    "index": 165,
                    "name": "production-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 692060160
                  },
                  {
                    "index": 166,
                    "name": "utility-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 696254464
                  },
                  {
                    "index": 167,
                    "name": "space-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 700448768
                  },
                  {
                    "index": 168,
                    "name": "pistol",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 704643072
                  },
                  {
                    "index": 169,
                    "name": "submachine-gun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 708837376
                  },
                  {
                    "index": 170,
                    "name": "shotgun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 713031680
                  },
                  {
                    "index": 171,
                    "name": "combat-shotgun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 717225984
                  },
                  {
                    "index": 172,
                    "name": "rocket-launcher",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 721420288
                  },
                  {
                    "index": 173,
                    "name": "flamethrower",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 725614592
                  },
                  {
                    "index": 174,
                    "name": "firearm-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 729808896
                  },
                  {
                    "index": 175,
                    "name": "piercing-rounds-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 734003200
                  },
                  {
                    "index": 176,
                    "name": "uranium-rounds-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 738197504
                  },
                  {
                    "index": 177,
                    "type": "recipe",
                    "name": "advanced-oil-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 742391808
                  },
                  {
                    "index": 178,
                    "name": "piercing-shotgun-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 746586112
                  },
                  {
                    "index": 179,
                    "name": "cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 750780416
                  },
                  {
                    "index": 180,
                    "name": "explosive-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 754974720
                  },
                  {
                    "index": 181,
                    "name": "uranium-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 759169024
                  },
                  {
                    "index": 182,
                    "name": "explosive-uranium-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 763363328
                  },
                  {
                    "index": 183,
                    "name": "artillery-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 767557632
                  },
                  {
                    "index": 184,
                    "name": "rocket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 771751936
                  },
                  {
                    "index": 185,
                    "name": "assembling-machine-1",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 775946240
                  },
                  {
                    "index": 186,
                    "name": "flamethrower-ammo",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 780140544
                  },
                  {
                    "index": 187,
                    "name": "grenade",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 784334848
                  },
                  {
                    "index": 188,
                    "name": "cluster-grenade",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 788529152
                  },
                  {
                    "index": 189,
                    "name": "poison-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 792723456
                  },
                  {
                    "index": 190,
                    "name": "slowdown-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 796917760
                  },
                  {
                    "index": 191,
                    "name": "defender-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 801112064
                  },
                  {
                    "index": 192,
                    "type": "entity",
                    "name": "defender",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 805306368
                  },
                  {
                    "index": 193,
                    "type": "entity",
                    "name": "distractor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 809500672
                  },
                  {
                    "index": 194,
                    "name": "wood",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 813694976
                  },
                  {
                    "index": 195,
                    "name": "pipe-to-ground",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 817889280
                  },
                  {
                    "index": 196,
                    "name": "destroyer-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 822083584
                  },
                  {
                    "index": 197,
                    "name": "light-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 826277888
                  },
                  {
                    "index": 198,
                    "name": "heavy-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 830472192
                  },
                  {
                    "index": 199,
                    "name": "modular-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 834666496
                  },
                  {
                    "index": 200,
                    "name": "power-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 838860800
                  },
                  {
                    "index": 201,
                    "name": "power-armor-mk2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 843055104
                  },
                  {
                    "index": 202,
                    "name": "heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 847249408
                  },
                  {
                    "index": 203,
                    "name": "fission-reactor-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 851443712
                  },
                  {
                    "index": 204,
                    "name": "battery-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 855638016
                  },
                  {
                    "index": 205,
                    "name": "pipe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 859832320
                  },
                  {
                    "index": 206,
                    "type": "recipe",
                    "name": "water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 864026624
                  },
                  {
                    "index": 207,
                    "name": "exoskeleton-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 868220928
                  },
                  {
                    "index": 208,
                    "name": "personal-roboport-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 872415232
                  },
                  {
                    "index": 209,
                    "name": "personal-roboport-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 876609536
                  },
                  {
                    "index": 210,
                    "name": "night-vision-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 880803840
                  },
                  {
                    "index": 211,
                    "name": "energy-shield-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 884998144
                  },
                  {
                    "index": 212,
                    "name": "energy-shield-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 889192448
                  },
                  {
                    "index": 213,
                    "name": "personal-laser-defense-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 893386752
                  },
                  {
                    "index": 214,
                    "name": "discharge-defense-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 897581056
                  },
                  {
                    "index": 215,
                    "name": "stone-wall",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 901775360
                  },
                  {
                    "index": 216,
                    "name": "gate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 905969664
                  },
                  {
                    "index": 217,
                    "name": "radar",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 910163968
                  },
                  {
                    "index": 218,
                    "name": "land-mine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 914358272
                  },
                  {
                    "index": 219,
                    "name": "gun-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 918552576
                  },
                  {
                    "index": 220,
                    "name": "laser-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 922746880
                  },
                  {
                    "index": 221,
                    "name": "flamethrower-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 926941184
                  },
                  {
                    "index": 222,
                    "name": "artillery-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 931135488
                  },
                  {
                    "index": 223,
                    "type": "fluid",
                    "name": "water",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 935329792
                  },
                  {
                    "index": 224,
                    "type": "fluid",
                    "name": "steam",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 939524096
                  },
                  {
                    "index": 225,
                    "type": "fluid",
                    "name": "crude-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 943718400
                  },
                  {
                    "index": 226,
                    "type": "fluid",
                    "name": "petroleum-gas",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 947912704
                  },
                  {
                    "index": 227,
                    "type": "fluid",
                    "name": "light-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 952107008
                  },
                  {
                    "index": 228,
                    "type": "fluid",
                    "name": "heavy-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 956301312
                  },
                  {
                    "index": 229,
                    "type": "fluid",
                    "name": "lubricant",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 960495616
                  },
                  {
                    "index": 230,
                    "type": "fluid",
                    "name": "sulfuric-acid",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 964689920
                  },
                  {
                    "index": 231,
                    "type": "entity",
                    "name": "small-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 968884224
                  },
                  {
                    "index": 232,
                    "type": "entity",
                    "name": "medium-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 973078528
                  },
                  {
                    "index": 233,
                    "type": "entity",
                    "name": "big-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 977272832
                  },
                  {
                    "index": 234,
                    "type": "entity",
                    "name": "behemoth-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 981467136
                  },
                  {
                    "index": 235,
                    "type": "entity",
                    "name": "small-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 985661440
                  },
                  {
                    "index": 236,
                    "type": "entity",
                    "name": "medium-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 989855744
                  },
                  {
                    "index": 237,
                    "type": "entity",
                    "name": "big-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 994050048
                  },
                  {
                    "index": 238,
                    "type": "entity",
                    "name": "behemoth-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 998244352
                  },
                  {
                    "index": 239,
                    "type": "entity",
                    "name": "small-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1002438656
                  },
                  {
                    "index": 240,
                    "type": "entity",
                    "name": "medium-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1006632960
                  },
                  {
                    "index": 241,
                    "type": "entity",
                    "name": "big-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1010827264
                  },
                  {
                    "index": 242,
                    "type": "entity",
                    "name": "behemoth-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1015021568
                  },
                  {
                    "index": 243,
                    "type": "entity",
                    "name": "biter-spawner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1019215872
                  },
                  {
                    "index": 244,
                    "type": "entity",
                    "name": "spitter-spawner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1023410176
                  },
                  {
                    "index": 245,
                    "type": "entity",
                    "name": "cliff",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1027604480
                  },
                  {
                    "index": 246,
                    "type": "entity",
                    "name": "character",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1031798784
                  },
                  {
                    "index": 247,
                    "type": "entity",
                    "name": "big-sand-rock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1035993088
                  },
                  {
                    "index": 248,
                    "type": "entity",
                    "name": "huge-rock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1040187392
                  },
                  {
                    "index": 249,
                    "type": "entity",
                    "name": "crude-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1044381696
                  },
                  {
                    "index": 250,
                    "name": "copper-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1048576000
                  },
                  {
                    "index": 251,
                    "name": "green-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1052770304
                  },
                  {
                    "index": 252,
                    "name": "red-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1056964608
                  },
                  {
                    "index": 253,
                    "name": "spidertron-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1061158912
                  },
                  {
                    "index": 254,
                    "name": "discharge-defense-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1065353216
                  },
                  {
                    "index": 255,
                    "name": "artillery-targeting-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1069547520
                  },
                  {
                    "index": 256,
                    "type": "entity",
                    "name": "entity-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1073741824
                  },
                  {
                    "index": 257,
                    "type": "entity",
                    "name": "item-on-ground",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1077936128
                  },
                  {
                    "index": 258,
                    "type": "entity",
                    "name": "item-request-proxy",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1082130432
                  },
                  {
                    "index": 259,
                    "type": "entity",
                    "name": "tile-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1086324736
                  },
                  {
                    "index": 260,
                    "type": "space-location",
                    "name": "nauvis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1090519040
                  },
                  {
                    "index": 261,
                    "type": "entity",
                    "name": "cargo-pod",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1094713344
                  },
                  {
                    "index": 262,
                    "type": "entity",
                    "name": "cargo-pod-container",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1098907648
                  },
                  {
                    "index": 263,
                    "name": "chemical-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1103101952
                  },
                  {
                    "index": 264,
                    "type": "entity",
                    "name": "destroyer",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1107296256
                  },
                  {
                    "index": 265,
                    "name": "explosive-rocket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1111490560
                  },
                  {
                    "index": 266,
                    "name": "electronic-circuit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1115684864
                  },
                  {
                    "index": 267,
                    "name": "belt-immunity-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1119879168
                  },
                  {
                    "index": 268,
                    "name": "shotgun-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1124073472
                  },
                  {
                    "index": 269,
                    "name": "battery-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1128267776
                  },
                  {
                    "index": 270,
                    "name": "heat-pipe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1132462080
                  },
                  {
                    "index": 271,
                    "name": "atomic-bomb",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1136656384
                  },
                  {
                    "index": 272,
                    "name": "distractor-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1140850688
                  },
                  {
                    "index": 273,
                    "type": "virtual",
                    "name": "signal-A",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1145044992
                  },
                  {
                    "index": 274,
                    "type": "virtual",
                    "name": "signal-B",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1149239296
                  },
                  {
                    "index": 275,
                    "type": "virtual",
                    "name": "signal-D",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1157627904
                  },
                  {
                    "index": 276,
                    "type": "virtual",
                    "name": "signal-E",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1161822208
                  },
                  {
                    "index": 277,
                    "type": "virtual",
                    "name": "signal-F",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1166016512
                  },
                  {
                    "index": 278,
                    "type": "virtual",
                    "name": "signal-G",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1170210816
                  },
                  {
                    "index": 279,
                    "type": "virtual",
                    "name": "signal-H",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1174405120
                  },
                  {
                    "index": 280,
                    "name": "solar-panel-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1178599424
                  },
                  {
                    "index": 281,
                    "type": "virtual",
                    "name": "signal-J",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1182793728
                  },
                  {
                    "index": 282,
                    "type": "virtual",
                    "name": "signal-K",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1186988032
                  },
                  {
                    "index": 283,
                    "type": "virtual",
                    "name": "signal-L",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1191182336
                  },
                  {
                    "index": 284,
                    "type": "virtual",
                    "name": "signal-M",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1195376640
                  },
                  {
                    "index": 285,
                    "type": "virtual",
                    "name": "signal-N",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1199570944
                  },
                  {
                    "index": 286,
                    "type": "virtual",
                    "name": "signal-O",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1203765248
                  },
                  {
                    "index": 287,
                    "type": "virtual",
                    "name": "signal-P",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1207959552
                  },
                  {
                    "index": 288,
                    "type": "virtual",
                    "name": "signal-Q",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1212153856
                  },
                  {
                    "index": 289,
                    "type": "virtual",
                    "name": "signal-R",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1216348160
                  },
                  {
                    "index": 290,
                    "type": "virtual",
                    "name": "signal-T",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1224736768
                  },
                  {
                    "index": 291,
                    "type": "virtual",
                    "name": "signal-U",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1228931072
                  },
                  {
                    "index": 292,
                    "type": "virtual",
                    "name": "signal-V",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1233125376
                  },
                  {
                    "index": 293,
                    "type": "virtual",
                    "name": "signal-W",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1237319680
                  },
                  {
                    "index": 294,
                    "type": "virtual",
                    "name": "signal-X",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1241513984
                  },
                  {
                    "index": 295,
                    "type": "virtual",
                    "name": "signal-Y",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1245708288
                  },
                  {
                    "index": 296,
                    "type": "virtual",
                    "name": "signal-Z",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1249902592
                  },
                  {
                    "index": 297,
                    "type": "virtual",
                    "name": "signal-comma",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1254096896
                  },
                  {
                    "index": 298,
                    "type": "virtual",
                    "name": "signal-letter-dot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1258291200
                  },
                  {
                    "index": 299,
                    "type": "virtual",
                    "name": "signal-exclamation-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1262485504
                  },
                  {
                    "index": 300,
                    "type": "virtual",
                    "name": "signal-question-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1266679808
                  },
                  {
                    "index": 301,
                    "type": "virtual",
                    "name": "signal-colon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1270874112
                  },
                  {
                    "index": 302,
                    "type": "virtual",
                    "name": "signal-apostrophe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1275068416
                  },
                  {
                    "index": 303,
                    "type": "virtual",
                    "name": "signal-quotation-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1279262720
                  },
                  {
                    "index": 304,
                    "type": "virtual",
                    "name": "signal-ampersand",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1283457024
                  },
                  {
                    "index": 305,
                    "type": "virtual",
                    "name": "signal-circumflex-accent",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1287651328
                  },
                  {
                    "index": 306,
                    "type": "virtual",
                    "name": "signal-number-sign",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1291845632
                  },
                  {
                    "index": 307,
                    "type": "virtual",
                    "name": "signal-multiplication",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1296039936
                  },
                  {
                    "index": 308,
                    "type": "virtual",
                    "name": "signal-division",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1300234240
                  },
                  {
                    "index": 309,
                    "type": "virtual",
                    "name": "signal-equal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1304428544
                  },
                  {
                    "index": 310,
                    "type": "virtual",
                    "name": "signal-not-equal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1308622848
                  },
                  {
                    "index": 311,
                    "type": "virtual",
                    "name": "signal-less-than",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1312817152
                  },
                  {
                    "index": 312,
                    "type": "virtual",
                    "name": "signal-greater-than",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1317011456
                  },
                  {
                    "index": 313,
                    "type": "virtual",
                    "name": "signal-less-than-or-equal-to",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1321205760
                  },
                  {
                    "index": 314,
                    "type": "virtual",
                    "name": "signal-greater-than-or-equal-to",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1325400064
                  },
                  {
                    "index": 315,
                    "type": "virtual",
                    "name": "signal-left-parenthesis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1329594368
                  },
                  {
                    "index": 316,
                    "type": "virtual",
                    "name": "signal-right-parenthesis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1333788672
                  },
                  {
                    "index": 317,
                    "type": "virtual",
                    "name": "signal-left-square-bracket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1337982976
                  },
                  {
                    "index": 318,
                    "type": "virtual",
                    "name": "signal-right-square-bracket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1342177280
                  },
                  {
                    "index": 319,
                    "type": "virtual",
                    "name": "signal-blue",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1354760192
                  },
                  {
                    "index": 320,
                    "type": "virtual",
                    "name": "signal-cyan",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1358954496
                  },
                  {
                    "index": 321,
                    "type": "virtual",
                    "name": "signal-pink",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1363148800
                  },
                  {
                    "index": 322,
                    "type": "virtual",
                    "name": "signal-yellow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1367343104
                  },
                  {
                    "index": 323,
                    "type": "virtual",
                    "name": "signal-white",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1371537408
                  },
                  {
                    "index": 324,
                    "type": "virtual",
                    "name": "signal-grey",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1375731712
                  },
                  {
                    "index": 325,
                    "type": "virtual",
                    "name": "signal-black",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1379926016
                  },
                  {
                    "index": 326,
                    "type": "virtual",
                    "name": "signal-check",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1384120320
                  },
                  {
                    "index": 327,
                    "type": "virtual",
                    "name": "signal-I",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1388314624
                  },
                  {
                    "index": 328,
                    "type": "virtual",
                    "name": "signal-no-entry",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1392508928
                  },
                  {
                    "index": 329,
                    "type": "virtual",
                    "name": "signal-heart",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1396703232
                  },
                  {
                    "index": 330,
                    "type": "virtual",
                    "name": "signal-alert",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1400897536
                  },
                  {
                    "index": 331,
                    "type": "virtual",
                    "name": "signal-star",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1405091840
                  },
                  {
                    "index": 332,
                    "type": "virtual",
                    "name": "signal-info",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1409286144
                  },
                  {
                    "index": 333,
                    "type": "virtual",
                    "name": "shape-vertical",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1413480448
                  },
                  {
                    "index": 334,
                    "type": "virtual",
                    "name": "shape-horizontal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1417674752
                  },
                  {
                    "index": 335,
                    "type": "virtual",
                    "name": "shape-curve",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1421869056
                  },
                  {
                    "index": 336,
                    "type": "virtual",
                    "name": "shape-curve-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1426063360
                  },
                  {
                    "index": 337,
                    "type": "virtual",
                    "name": "shape-corner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1430257664
                  },
                  {
                    "index": 338,
                    "type": "virtual",
                    "name": "shape-corner-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1434451968
                  },
                  {
                    "index": 339,
                    "type": "virtual",
                    "name": "shape-t",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1438646272
                  },
                  {
                    "index": 340,
                    "type": "virtual",
                    "name": "shape-t-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1442840576
                  },
                  {
                    "index": 341,
                    "type": "virtual",
                    "name": "shape-cross",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1447034880
                  },
                  {
                    "index": 342,
                    "type": "virtual",
                    "name": "shape-diagonal-cross",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1451229184
                  },
                  {
                    "index": 343,
                    "type": "virtual",
                    "name": "shape-diagonal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1455423488
                  },
                  {
                    "index": 344,
                    "type": "virtual",
                    "name": "shape-diagonal-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1459617792
                  },
                  {
                    "index": 345,
                    "type": "virtual",
                    "name": "shape-curve-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1463812096
                  },
                  {
                    "index": 346,
                    "type": "virtual",
                    "name": "shape-curve-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1468006400
                  },
                  {
                    "index": 347,
                    "type": "virtual",
                    "name": "shape-corner-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1472200704
                  },
                  {
                    "index": 348,
                    "type": "virtual",
                    "name": "shape-corner-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1476395008
                  },
                  {
                    "index": 349,
                    "type": "virtual",
                    "name": "shape-t-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1480589312
                  },
                  {
                    "index": 350,
                    "type": "virtual",
                    "name": "shape-t-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1484783616
                  },
                  {
                    "index": 351,
                    "name": "iron-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1488977920
                  },
                  {
                    "index": 352,
                    "name": "splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1493172224
                  },
                  {
                    "index": 353,
                    "type": "virtual",
                    "name": "up-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1497366528
                  },
                  {
                    "index": 354,
                    "type": "virtual",
                    "name": "up-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1501560832
                  },
                  {
                    "index": 355,
                    "type": "virtual",
                    "name": "right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1505755136
                  },
                  {
                    "index": 356,
                    "type": "virtual",
                    "name": "down-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1509949440
                  },
                  {
                    "index": 357,
                    "type": "virtual",
                    "name": "down-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1514143744
                  },
                  {
                    "index": 358,
                    "type": "virtual",
                    "name": "down-left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1518338048
                  },
                  {
                    "index": 359,
                    "type": "virtual",
                    "name": "left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1522532352
                  },
                  {
                    "index": 360,
                    "type": "virtual",
                    "name": "up-left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1526726656
                  },
                  {
                    "index": 361,
                    "type": "virtual",
                    "name": "signal-rightwards-leftwards-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1530920960
                  },
                  {
                    "index": 362,
                    "type": "virtual",
                    "name": "signal-upwards-downwards-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1535115264
                  },
                  {
                    "index": 363,
                    "name": "rail-signal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1539309568
                  },
                  {
                    "index": 364,
                    "type": "virtual",
                    "name": "signal-left-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1543503872
                  },
                  {
                    "index": 365,
                    "type": "virtual",
                    "name": "signal-up-down-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1547698176
                  },
                  {
                    "index": 366,
                    "name": "train-stop",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1551892480
                  },
                  {
                    "index": 367,
                    "type": "virtual",
                    "name": "signal-anticlockwise-circle-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1556086784
                  },
                  {
                    "index": 368,
                    "type": "virtual",
                    "name": "signal-input",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1560281088
                  },
                  {
                    "index": 369,
                    "type": "virtual",
                    "name": "signal-output",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1564475392
                  },
                  {
                    "index": 370,
                    "type": "virtual",
                    "name": "signal-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1568669696
                  },
                  {
                    "index": 371,
                    "type": "virtual",
                    "name": "signal-lightning",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1572864000
                  },
                  {
                    "index": 372,
                    "name": "small-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1577058304
                  },
                  {
                    "index": 373,
                    "name": "medium-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1581252608
                  },
                  {
                    "index": 374,
                    "name": "big-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1585446912
                  },
                  {
                    "index": 375,
                    "type": "virtual",
                    "name": "signal-radioactivity",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1589641216
                  },
                  {
                    "index": 376,
                    "type": "virtual",
                    "name": "signal-thermometer-blue",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1593835520
                  },
                  {
                    "index": 377,
                    "type": "virtual",
                    "name": "signal-thermometer-red",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1598029824
                  },
                  {
                    "index": 378,
                    "type": "virtual",
                    "name": "signal-fire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1602224128
                  },
                  {
                    "index": 379,
                    "type": "virtual",
                    "name": "signal-snowflake",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1606418432
                  },
                  {
                    "index": 380,
                    "type": "virtual",
                    "name": "signal-explosion",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1610612736
                  },
                  {
                    "index": 381,
                    "type": "virtual",
                    "name": "signal-liquid",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1614807040
                  },
                  {
                    "index": 382,
                    "name": "rail",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1619001344
                  },
                  {
                    "index": 383,
                    "name": "rail-chain-signal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1623195648
                  },
                  {
                    "index": 384,
                    "type": "virtual",
                    "name": "signal-trash-bin",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1627389952
                  },
                  {
                    "index": 385,
                    "type": "virtual",
                    "name": "signal-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1631584256
                  },
                  {
                    "index": 386,
                    "type": "virtual",
                    "name": "signal-map-marker",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1635778560
                  },
                  {
                    "index": 387,
                    "type": "virtual",
                    "name": "signal-white-flag",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1639972864
                  },
                  {
                    "index": 388,
                    "type": "virtual",
                    "name": "signal-lock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1644167168
                  },
                  {
                    "index": 389,
                    "type": "virtual",
                    "name": "signal-unlock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1648361472
                  },
                  {
                    "index": 390,
                    "type": "virtual",
                    "name": "signal-speed",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1652555776
                  },
                  {
                    "index": 391,
                    "type": "virtual",
                    "name": "signal-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1656750080
                  },
                  {
                    "index": 392,
                    "type": "virtual",
                    "name": "signal-hourglass",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1660944384
                  },
                  {
                    "index": 393,
                    "type": "virtual",
                    "name": "signal-alarm",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1665138688
                  },
                  {
                    "index": 394,
                    "type": "virtual",
                    "name": "signal-sun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1669332992
                  },
                  {
                    "index": 395,
                    "type": "virtual",
                    "name": "signal-moon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1673527296
                  },
                  {
                    "index": 396,
                    "type": "virtual",
                    "name": "signal-mining",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1677721600
                  },
                  {
                    "index": 397,
                    "type": "virtual",
                    "name": "signal-skull",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1681915904
                  },
                  {
                    "index": 398,
                    "type": "virtual",
                    "name": "signal-damage",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1686110208
                  },
                  {
                    "index": 399,
                    "type": "virtual",
                    "name": "signal-weapon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1690304512
                  }
                ]
              }
            ]
          }
        }
      },
      {
        "entity_number": 2,
        "name": "constant-combinator",
        "position": {
          "x": 562.5,
          "y": -23.5
        },
        "direction": 4,
        "control_behavior": {
          "sections": {
            "sections": [
              {
                "index": 1,
                "filters": [
                  {
                    "index": 1,
                    "type": "virtual",
                    "name": "signal-deny",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 4194304
                  },
                  {
                    "index": 2,
                    "type": "virtual",
                    "name": "signal-0",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 8388608
                  },
                  {
                    "index": 3,
                    "type": "virtual",
                    "name": "signal-1",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 12582912
                  },
                  {
                    "index": 4,
                    "type": "virtual",
                    "name": "signal-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 16777216
                  },
                  {
                    "index": 5,
                    "type": "virtual",
                    "name": "signal-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 20971520
                  },
                  {
                    "index": 6,
                    "type": "virtual",
                    "name": "signal-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 25165824
                  },
                  {
                    "index": 7,
                    "type": "virtual",
                    "name": "signal-5",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 29360128
                  },
                  {
                    "index": 8,
                    "type": "virtual",
                    "name": "signal-6",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 33554432
                  },
                  {
                    "index": 9,
                    "type": "virtual",
                    "name": "signal-7",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 37748736
                  },
                  {
                    "index": 10,
                    "type": "virtual",
                    "name": "signal-8",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 41943040
                  },
                  {
                    "index": 11,
                    "type": "virtual",
                    "name": "signal-9",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 46137344
                  },
                  {
                    "index": 12,
                    "type": "virtual",
                    "name": "signal-dot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 50331648
                  },
                  {
                    "index": 13,
                    "type": "virtual",
                    "name": "shape-circle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 54525952
                  },
                  {
                    "index": 14,
                    "name": "burner-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 58720256
                  },
                  {
                    "index": 15,
                    "name": "inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 62914560
                  },
                  {
                    "index": 16,
                    "name": "long-handed-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 67108864
                  },
                  {
                    "index": 17,
                    "name": "fast-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 71303168
                  },
                  {
                    "index": 18,
                    "name": "bulk-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 75497472
                  },
                  {
                    "index": 19,
                    "name": "small-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 79691776
                  },
                  {
                    "index": 20,
                    "name": "medium-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 83886080
                  },
                  {
                    "index": 21,
                    "name": "big-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 88080384
                  },
                  {
                    "index": 22,
                    "name": "substation",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 92274688
                  },
                  {
                    "index": 23,
                    "name": "pipe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 96468992
                  },
                  {
                    "index": 24,
                    "name": "pipe-to-ground",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 100663296
                  },
                  {
                    "index": 25,
                    "name": "pump",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 104857600
                  },
                  {
                    "index": 26,
                    "name": "rail",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 109051904
                  },
                  {
                    "index": 27,
                    "name": "train-stop",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 113246208
                  },
                  {
                    "index": 28,
                    "name": "rail-signal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 117440512
                  },
                  {
                    "index": 29,
                    "name": "rail-chain-signal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 121634816
                  },
                  {
                    "index": 30,
                    "name": "locomotive",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 125829120
                  },
                  {
                    "index": 31,
                    "name": "cargo-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 130023424
                  },
                  {
                    "index": 32,
                    "name": "fluid-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 134217728
                  },
                  {
                    "index": 33,
                    "name": "artillery-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 138412032
                  },
                  {
                    "index": 34,
                    "name": "car",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 142606336
                  },
                  {
                    "index": 35,
                    "name": "tank",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 146800640
                  },
                  {
                    "index": 36,
                    "name": "spidertron",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 150994944
                  },
                  {
                    "index": 37,
                    "name": "underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 155189248
                  },
                  {
                    "index": 38,
                    "name": "construction-robot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 159383552
                  },
                  {
                    "index": 39,
                    "name": "active-provider-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 163577856
                  },
                  {
                    "index": 40,
                    "name": "passive-provider-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 167772160
                  },
                  {
                    "index": 41,
                    "name": "small-lamp",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 171966464
                  },
                  {
                    "index": 42,
                    "name": "arithmetic-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 176160768
                  },
                  {
                    "index": 43,
                    "name": "fast-splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 180355072
                  },
                  {
                    "index": 44,
                    "name": "selector-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 184549376
                  },
                  {
                    "index": 45,
                    "name": "storage-tank",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 188743680
                  },
                  {
                    "index": 46,
                    "name": "express-transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 192937984
                  },
                  {
                    "index": 47,
                    "name": "programmable-speaker",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 197132288
                  },
                  {
                    "index": 48,
                    "name": "display-panel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 201326592
                  },
                  {
                    "index": 49,
                    "name": "stone-brick",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 205520896
                  },
                  {
                    "index": 50,
                    "name": "concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 209715200
                  },
                  {
                    "index": 51,
                    "name": "hazard-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 213909504
                  },
                  {
                    "index": 52,
                    "name": "refined-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 218103808
                  },
                  {
                    "index": 53,
                    "name": "refined-hazard-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 222298112
                  },
                  {
                    "index": 54,
                    "name": "landfill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 226492416
                  },
                  {
                    "index": 55,
                    "name": "cliff-explosives",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 230686720,
                    "import_from": "nauvis"
                  },
                  {
                    "index": 56,
                    "name": "repair-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 234881024
                  },
                  {
                    "index": 57,
                    "name": "blueprint",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 239075328
                  },
                  {
                    "index": 58,
                    "name": "deconstruction-planner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 243269632
                  },
                  {
                    "index": 59,
                    "name": "upgrade-planner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 247463936
                  },
                  {
                    "index": 60,
                    "name": "blueprint-book",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 251658240
                  },
                  {
                    "index": 61,
                    "name": "boiler",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 255852544
                  },
                  {
                    "index": 62,
                    "name": "steam-engine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 260046848
                  },
                  {
                    "index": 63,
                    "name": "solar-panel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 264241152
                  },
                  {
                    "index": 64,
                    "name": "accumulator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 268435456
                  },
                  {
                    "index": 65,
                    "name": "nuclear-reactor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 272629760
                  },
                  {
                    "index": 66,
                    "name": "express-underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 276824064
                  },
                  {
                    "index": 67,
                    "name": "heat-exchanger",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 281018368
                  },
                  {
                    "index": 68,
                    "name": "steam-turbine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 285212672
                  },
                  {
                    "index": 69,
                    "name": "burner-mining-drill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 289406976
                  },
                  {
                    "index": 70,
                    "name": "electric-mining-drill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 293601280
                  },
                  {
                    "index": 71,
                    "name": "offshore-pump",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 297795584
                  },
                  {
                    "index": 72,
                    "name": "pumpjack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 301989888
                  },
                  {
                    "index": 73,
                    "name": "stone-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 306184192
                  },
                  {
                    "index": 74,
                    "name": "steel-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 310378496
                  },
                  {
                    "index": 75,
                    "name": "electric-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 314572800
                  },
                  {
                    "index": 76,
                    "name": "fast-underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 318767104
                  },
                  {
                    "index": 77,
                    "name": "assembling-machine-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 322961408
                  },
                  {
                    "index": 78,
                    "name": "assembling-machine-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 327155712
                  },
                  {
                    "index": 79,
                    "name": "oil-refinery",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 331350016
                  },
                  {
                    "index": 80,
                    "name": "chemical-plant",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 335544320
                  },
                  {
                    "index": 81,
                    "name": "centrifuge",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 339738624
                  },
                  {
                    "index": 82,
                    "name": "lab",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 343932928
                  },
                  {
                    "index": 83,
                    "name": "wooden-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 348127232
                  },
                  {
                    "index": 84,
                    "name": "speed-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 352321536
                  },
                  {
                    "index": 85,
                    "name": "speed-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 356515840
                  },
                  {
                    "index": 86,
                    "name": "speed-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 360710144
                  },
                  {
                    "index": 87,
                    "name": "efficiency-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 364904448
                  },
                  {
                    "index": 88,
                    "name": "efficiency-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 369098752
                  },
                  {
                    "index": 89,
                    "name": "efficiency-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 373293056
                  },
                  {
                    "index": 90,
                    "name": "productivity-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 377487360
                  },
                  {
                    "index": 91,
                    "name": "productivity-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 381681664
                  },
                  {
                    "index": 92,
                    "name": "productivity-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 385875968
                  },
                  {
                    "index": 93,
                    "name": "rocket-silo",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 390070272
                  },
                  {
                    "index": 94,
                    "name": "cargo-landing-pad",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 394264576
                  },
                  {
                    "index": 95,
                    "name": "steel-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 398458880
                  },
                  {
                    "index": 96,
                    "type": "recipe",
                    "name": "basic-oil-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 402653184
                  },
                  {
                    "index": 97,
                    "name": "logistic-robot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 406847488
                  },
                  {
                    "index": 98,
                    "type": "recipe",
                    "name": "coal-liquefaction",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 411041792
                  },
                  {
                    "index": 99,
                    "type": "recipe",
                    "name": "heavy-oil-cracking",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 415236096
                  },
                  {
                    "index": 100,
                    "type": "recipe",
                    "name": "light-oil-cracking",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 419430400
                  },
                  {
                    "index": 101,
                    "type": "recipe",
                    "name": "solid-fuel-from-petroleum-gas",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 423624704
                  },
                  {
                    "index": 102,
                    "type": "recipe",
                    "name": "solid-fuel-from-light-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 427819008
                  },
                  {
                    "index": 103,
                    "type": "recipe",
                    "name": "solid-fuel-from-heavy-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 432013312
                  },
                  {
                    "index": 104,
                    "name": "express-splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 436207616
                  },
                  {
                    "index": 105,
                    "name": "coal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 440401920
                  },
                  {
                    "index": 106,
                    "name": "stone",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 444596224
                  },
                  {
                    "index": 107,
                    "name": "iron-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 448790528
                  },
                  {
                    "index": 108,
                    "name": "copper-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 452984832
                  },
                  {
                    "index": 109,
                    "name": "uranium-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 457179136
                  },
                  {
                    "index": 110,
                    "name": "raw-fish",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 461373440
                  },
                  {
                    "index": 111,
                    "name": "iron-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 465567744
                  },
                  {
                    "index": 112,
                    "name": "copper-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 469762048
                  },
                  {
                    "index": 113,
                    "name": "steel-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 473956352
                  },
                  {
                    "index": 114,
                    "name": "solid-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 478150656
                  },
                  {
                    "index": 115,
                    "name": "plastic-bar",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 482344960
                  },
                  {
                    "index": 116,
                    "name": "sulfur",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 486539264
                  },
                  {
                    "index": 117,
                    "name": "battery",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 490733568
                  },
                  {
                    "index": 118,
                    "name": "explosives",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 494927872
                  },
                  {
                    "index": 119,
                    "name": "water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 499122176
                  },
                  {
                    "index": 120,
                    "name": "crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 503316480
                  },
                  {
                    "index": 121,
                    "name": "petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 507510784
                  },
                  {
                    "index": 122,
                    "name": "light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 511705088
                  },
                  {
                    "index": 123,
                    "name": "decider-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 515899392
                  },
                  {
                    "index": 124,
                    "name": "lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 520093696
                  },
                  {
                    "index": 125,
                    "name": "sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 524288000
                  },
                  {
                    "index": 126,
                    "name": "power-switch",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 528482304
                  },
                  {
                    "index": 127,
                    "type": "recipe",
                    "name": "crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 532676608
                  },
                  {
                    "index": 128,
                    "type": "recipe",
                    "name": "petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 536870912
                  },
                  {
                    "index": 129,
                    "type": "recipe",
                    "name": "light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 541065216
                  },
                  {
                    "index": 130,
                    "type": "recipe",
                    "name": "heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 545259520
                  },
                  {
                    "index": 131,
                    "type": "recipe",
                    "name": "lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 549453824
                  },
                  {
                    "index": 132,
                    "type": "recipe",
                    "name": "sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 553648128
                  },
                  {
                    "index": 133,
                    "type": "recipe",
                    "name": "empty-water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 557842432
                  },
                  {
                    "index": 134,
                    "type": "recipe",
                    "name": "empty-crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 562036736
                  },
                  {
                    "index": 135,
                    "type": "recipe",
                    "name": "empty-petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 566231040
                  },
                  {
                    "index": 136,
                    "type": "recipe",
                    "name": "empty-light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 570425344
                  },
                  {
                    "index": 137,
                    "type": "recipe",
                    "name": "empty-heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 574619648
                  },
                  {
                    "index": 138,
                    "type": "recipe",
                    "name": "empty-lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 578813952
                  },
                  {
                    "index": 139,
                    "type": "recipe",
                    "name": "empty-sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 583008256
                  },
                  {
                    "index": 140,
                    "name": "iron-gear-wheel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 587202560
                  },
                  {
                    "index": 141,
                    "name": "iron-stick",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 591396864
                  },
                  {
                    "index": 142,
                    "name": "copper-cable",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 595591168
                  },
                  {
                    "index": 143,
                    "name": "barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 599785472
                  },
                  {
                    "index": 144,
                    "name": "constant-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 603979776
                  },
                  {
                    "index": 145,
                    "name": "advanced-circuit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 608174080
                  },
                  {
                    "index": 146,
                    "name": "processing-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 612368384
                  },
                  {
                    "index": 147,
                    "name": "engine-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 616562688
                  },
                  {
                    "index": 148,
                    "name": "electric-engine-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 620756992
                  },
                  {
                    "index": 149,
                    "name": "flying-robot-frame",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 624951296
                  },
                  {
                    "index": 150,
                    "name": "low-density-structure",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 629145600
                  },
                  {
                    "index": 151,
                    "name": "rocket-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 633339904
                  },
                  {
                    "index": 152,
                    "type": "recipe",
                    "name": "rocket-part",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 637534208
                  },
                  {
                    "index": 153,
                    "type": "recipe",
                    "name": "uranium-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 641728512
                  },
                  {
                    "index": 154,
                    "name": "uranium-235",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 645922816
                  },
                  {
                    "index": 155,
                    "name": "uranium-238",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 650117120
                  },
                  {
                    "index": 156,
                    "name": "uranium-fuel-cell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 654311424
                  },
                  {
                    "index": 157,
                    "name": "depleted-uranium-fuel-cell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 658505728
                  },
                  {
                    "index": 158,
                    "type": "recipe",
                    "name": "nuclear-fuel-reprocessing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 662700032
                  },
                  {
                    "index": 159,
                    "type": "recipe",
                    "name": "kovarex-enrichment-process",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 666894336
                  },
                  {
                    "index": 160,
                    "name": "nuclear-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 671088640
                  },
                  {
                    "index": 161,
                    "name": "automation-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 675282944
                  },
                  {
                    "index": 162,
                    "name": "logistic-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 679477248
                  },
                  {
                    "index": 163,
                    "name": "military-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 683671552
                  },
                  {
                    "index": 164,
                    "name": "beacon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 687865856
                  },
                  {
                    "index": 165,
                    "name": "production-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 692060160
                  },
                  {
                    "index": 166,
                    "name": "utility-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 696254464
                  },
                  {
                    "index": 167,
                    "name": "space-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 700448768
                  },
                  {
                    "index": 168,
                    "name": "pistol",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 704643072
                  },
                  {
                    "index": 169,
                    "name": "submachine-gun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 708837376
                  },
                  {
                    "index": 170,
                    "name": "shotgun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 713031680
                  },
                  {
                    "index": 171,
                    "name": "combat-shotgun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 717225984
                  },
                  {
                    "index": 172,
                    "name": "rocket-launcher",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 721420288
                  },
                  {
                    "index": 173,
                    "name": "flamethrower",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 725614592
                  },
                  {
                    "index": 174,
                    "name": "firearm-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 729808896
                  },
                  {
                    "index": 175,
                    "name": "piercing-rounds-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 734003200
                  },
                  {
                    "index": 176,
                    "name": "uranium-rounds-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 738197504
                  },
                  {
                    "index": 177,
                    "type": "recipe",
                    "name": "advanced-oil-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 742391808
                  },
                  {
                    "index": 178,
                    "name": "piercing-shotgun-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 746586112
                  },
                  {
                    "index": 179,
                    "name": "cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 750780416
                  },
                  {
                    "index": 180,
                    "name": "explosive-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 754974720
                  },
                  {
                    "index": 181,
                    "name": "uranium-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 759169024
                  },
                  {
                    "index": 182,
                    "name": "explosive-uranium-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 763363328
                  },
                  {
                    "index": 183,
                    "name": "artillery-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 767557632
                  },
                  {
                    "index": 184,
                    "name": "rocket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 771751936
                  },
                  {
                    "index": 185,
                    "name": "assembling-machine-1",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 775946240
                  },
                  {
                    "index": 186,
                    "name": "flamethrower-ammo",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 780140544
                  },
                  {
                    "index": 187,
                    "name": "grenade",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 784334848
                  },
                  {
                    "index": 188,
                    "name": "cluster-grenade",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 788529152
                  },
                  {
                    "index": 189,
                    "name": "poison-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 792723456
                  },
                  {
                    "index": 190,
                    "name": "slowdown-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 796917760
                  },
                  {
                    "index": 191,
                    "name": "defender-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 801112064
                  },
                  {
                    "index": 192,
                    "type": "entity",
                    "name": "defender",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 805306368
                  },
                  {
                    "index": 193,
                    "type": "entity",
                    "name": "distractor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 809500672
                  },
                  {
                    "index": 194,
                    "name": "wood",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 813694976
                  },
                  {
                    "index": 195,
                    "name": "fast-transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 817889280
                  },
                  {
                    "index": 196,
                    "name": "destroyer-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 822083584
                  },
                  {
                    "index": 197,
                    "name": "light-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 826277888
                  },
                  {
                    "index": 198,
                    "name": "heavy-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 830472192
                  },
                  {
                    "index": 199,
                    "name": "modular-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 834666496
                  },
                  {
                    "index": 200,
                    "name": "power-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 838860800
                  },
                  {
                    "index": 201,
                    "name": "power-armor-mk2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 843055104
                  },
                  {
                    "index": 202,
                    "name": "heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 847249408
                  },
                  {
                    "index": 203,
                    "name": "fission-reactor-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 851443712
                  },
                  {
                    "index": 204,
                    "name": "battery-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 855638016
                  },
                  {
                    "index": 205,
                    "name": "transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 859832320
                  },
                  {
                    "index": 206,
                    "type": "recipe",
                    "name": "water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 864026624
                  },
                  {
                    "index": 207,
                    "name": "exoskeleton-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 868220928
                  },
                  {
                    "index": 208,
                    "name": "personal-roboport-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 872415232
                  },
                  {
                    "index": 209,
                    "name": "personal-roboport-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 876609536
                  },
                  {
                    "index": 210,
                    "name": "night-vision-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 880803840
                  },
                  {
                    "index": 211,
                    "name": "energy-shield-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 884998144
                  },
                  {
                    "index": 212,
                    "name": "energy-shield-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 889192448
                  },
                  {
                    "index": 213,
                    "name": "personal-laser-defense-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 893386752
                  },
                  {
                    "index": 214,
                    "name": "discharge-defense-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 897581056
                  },
                  {
                    "index": 215,
                    "name": "stone-wall",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 901775360
                  },
                  {
                    "index": 216,
                    "name": "gate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 905969664
                  },
                  {
                    "index": 217,
                    "name": "radar",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 910163968
                  },
                  {
                    "index": 218,
                    "name": "land-mine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 914358272
                  },
                  {
                    "index": 219,
                    "name": "gun-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 918552576
                  },
                  {
                    "index": 220,
                    "name": "laser-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 922746880
                  },
                  {
                    "index": 221,
                    "name": "flamethrower-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 926941184
                  },
                  {
                    "index": 222,
                    "name": "artillery-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 931135488
                  },
                  {
                    "index": 223,
                    "type": "fluid",
                    "name": "water",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 935329792
                  },
                  {
                    "index": 224,
                    "type": "fluid",
                    "name": "steam",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 939524096
                  },
                  {
                    "index": 225,
                    "type": "fluid",
                    "name": "crude-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 943718400
                  },
                  {
                    "index": 226,
                    "type": "fluid",
                    "name": "petroleum-gas",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 947912704
                  },
                  {
                    "index": 227,
                    "type": "fluid",
                    "name": "light-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 952107008
                  },
                  {
                    "index": 228,
                    "type": "fluid",
                    "name": "heavy-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 956301312
                  },
                  {
                    "index": 229,
                    "type": "fluid",
                    "name": "lubricant",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 960495616
                  },
                  {
                    "index": 230,
                    "type": "fluid",
                    "name": "sulfuric-acid",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 964689920
                  },
                  {
                    "index": 231,
                    "type": "entity",
                    "name": "small-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 968884224
                  },
                  {
                    "index": 232,
                    "type": "entity",
                    "name": "medium-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 973078528
                  },
                  {
                    "index": 233,
                    "type": "entity",
                    "name": "big-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 977272832
                  },
                  {
                    "index": 234,
                    "type": "entity",
                    "name": "behemoth-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 981467136
                  },
                  {
                    "index": 235,
                    "type": "entity",
                    "name": "small-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 985661440
                  },
                  {
                    "index": 236,
                    "type": "entity",
                    "name": "medium-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 989855744
                  },
                  {
                    "index": 237,
                    "type": "entity",
                    "name": "big-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 994050048
                  },
                  {
                    "index": 238,
                    "type": "entity",
                    "name": "behemoth-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 998244352
                  },
                  {
                    "index": 239,
                    "type": "entity",
                    "name": "small-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1002438656
                  },
                  {
                    "index": 240,
                    "type": "entity",
                    "name": "medium-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1006632960
                  },
                  {
                    "index": 241,
                    "type": "entity",
                    "name": "big-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1010827264
                  },
                  {
                    "index": 242,
                    "type": "entity",
                    "name": "behemoth-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1015021568
                  },
                  {
                    "index": 243,
                    "type": "entity",
                    "name": "biter-spawner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1019215872
                  },
                  {
                    "index": 244,
                    "type": "entity",
                    "name": "spitter-spawner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1023410176
                  },
                  {
                    "index": 245,
                    "type": "entity",
                    "name": "cliff",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1027604480
                  },
                  {
                    "index": 246,
                    "type": "entity",
                    "name": "character",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1031798784
                  },
                  {
                    "index": 247,
                    "type": "entity",
                    "name": "big-sand-rock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1035993088
                  },
                  {
                    "index": 248,
                    "type": "entity",
                    "name": "huge-rock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1040187392
                  },
                  {
                    "index": 249,
                    "type": "entity",
                    "name": "crude-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1044381696
                  },
                  {
                    "index": 250,
                    "name": "copper-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1048576000
                  },
                  {
                    "index": 251,
                    "name": "green-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1052770304
                  },
                  {
                    "index": 252,
                    "name": "red-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1056964608
                  },
                  {
                    "index": 253,
                    "name": "spidertron-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1061158912
                  },
                  {
                    "index": 254,
                    "name": "discharge-defense-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1065353216
                  },
                  {
                    "index": 255,
                    "name": "artillery-targeting-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1069547520
                  },
                  {
                    "index": 256,
                    "type": "entity",
                    "name": "entity-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1073741824
                  },
                  {
                    "index": 257,
                    "type": "entity",
                    "name": "item-on-ground",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1077936128
                  },
                  {
                    "index": 258,
                    "type": "entity",
                    "name": "item-request-proxy",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1082130432
                  },
                  {
                    "index": 259,
                    "type": "entity",
                    "name": "tile-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1086324736
                  },
                  {
                    "index": 260,
                    "type": "space-location",
                    "name": "nauvis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1090519040
                  },
                  {
                    "index": 261,
                    "type": "entity",
                    "name": "cargo-pod",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1094713344
                  },
                  {
                    "index": 262,
                    "type": "entity",
                    "name": "cargo-pod-container",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1098907648
                  },
                  {
                    "index": 263,
                    "name": "chemical-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1103101952
                  },
                  {
                    "index": 264,
                    "type": "entity",
                    "name": "destroyer",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1107296256
                  },
                  {
                    "index": 265,
                    "name": "explosive-rocket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1111490560
                  },
                  {
                    "index": 266,
                    "name": "electronic-circuit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1115684864
                  },
                  {
                    "index": 267,
                    "name": "belt-immunity-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1119879168
                  },
                  {
                    "index": 268,
                    "name": "shotgun-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1124073472
                  },
                  {
                    "index": 269,
                    "name": "battery-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1128267776
                  },
                  {
                    "index": 270,
                    "name": "heat-pipe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1132462080
                  },
                  {
                    "index": 271,
                    "name": "atomic-bomb",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1136656384
                  },
                  {
                    "index": 272,
                    "name": "distractor-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1140850688
                  },
                  {
                    "index": 273,
                    "type": "virtual",
                    "name": "signal-A",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1145044992
                  },
                  {
                    "index": 274,
                    "type": "virtual",
                    "name": "signal-B",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1149239296
                  },
                  {
                    "index": 275,
                    "type": "virtual",
                    "name": "signal-D",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1157627904
                  },
                  {
                    "index": 276,
                    "type": "virtual",
                    "name": "signal-E",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1161822208
                  },
                  {
                    "index": 277,
                    "type": "virtual",
                    "name": "signal-F",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1166016512
                  },
                  {
                    "index": 278,
                    "type": "virtual",
                    "name": "signal-G",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1170210816
                  },
                  {
                    "index": 279,
                    "type": "virtual",
                    "name": "signal-H",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1174405120
                  },
                  {
                    "index": 280,
                    "name": "solar-panel-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1178599424
                  },
                  {
                    "index": 281,
                    "type": "virtual",
                    "name": "signal-J",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1182793728
                  },
                  {
                    "index": 282,
                    "type": "virtual",
                    "name": "signal-K",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1186988032
                  },
                  {
                    "index": 283,
                    "type": "virtual",
                    "name": "signal-L",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1191182336
                  },
                  {
                    "index": 284,
                    "type": "virtual",
                    "name": "signal-M",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1195376640
                  },
                  {
                    "index": 285,
                    "type": "virtual",
                    "name": "signal-N",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1199570944
                  },
                  {
                    "index": 286,
                    "type": "virtual",
                    "name": "signal-O",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1203765248
                  },
                  {
                    "index": 287,
                    "type": "virtual",
                    "name": "signal-P",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1207959552
                  },
                  {
                    "index": 288,
                    "type": "virtual",
                    "name": "signal-Q",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1212153856
                  },
                  {
                    "index": 289,
                    "type": "virtual",
                    "name": "signal-R",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1216348160
                  },
                  {
                    "index": 290,
                    "type": "virtual",
                    "name": "signal-T",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1224736768
                  },
                  {
                    "index": 291,
                    "type": "virtual",
                    "name": "signal-U",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1228931072
                  },
                  {
                    "index": 292,
                    "type": "virtual",
                    "name": "signal-V",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1233125376
                  },
                  {
                    "index": 293,
                    "type": "virtual",
                    "name": "signal-W",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1237319680
                  },
                  {
                    "index": 294,
                    "type": "virtual",
                    "name": "signal-X",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1241513984
                  },
                  {
                    "index": 295,
                    "type": "virtual",
                    "name": "signal-Y",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1245708288
                  },
                  {
                    "index": 296,
                    "type": "virtual",
                    "name": "signal-Z",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1249902592
                  },
                  {
                    "index": 297,
                    "type": "virtual",
                    "name": "signal-comma",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1254096896
                  },
                  {
                    "index": 298,
                    "type": "virtual",
                    "name": "signal-letter-dot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1258291200
                  },
                  {
                    "index": 299,
                    "type": "virtual",
                    "name": "signal-exclamation-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1262485504
                  },
                  {
                    "index": 300,
                    "type": "virtual",
                    "name": "signal-question-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1266679808
                  },
                  {
                    "index": 301,
                    "type": "virtual",
                    "name": "signal-colon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1270874112
                  },
                  {
                    "index": 302,
                    "type": "virtual",
                    "name": "signal-apostrophe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1275068416
                  },
                  {
                    "index": 303,
                    "type": "virtual",
                    "name": "signal-quotation-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1279262720
                  },
                  {
                    "index": 304,
                    "type": "virtual",
                    "name": "signal-ampersand",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1283457024
                  },
                  {
                    "index": 305,
                    "type": "virtual",
                    "name": "signal-circumflex-accent",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1287651328
                  },
                  {
                    "index": 306,
                    "type": "virtual",
                    "name": "signal-number-sign",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1291845632
                  },
                  {
                    "index": 307,
                    "type": "virtual",
                    "name": "signal-multiplication",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1296039936
                  },
                  {
                    "index": 308,
                    "type": "virtual",
                    "name": "signal-division",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1300234240
                  },
                  {
                    "index": 309,
                    "type": "virtual",
                    "name": "signal-equal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1304428544
                  },
                  {
                    "index": 310,
                    "type": "virtual",
                    "name": "signal-not-equal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1308622848
                  },
                  {
                    "index": 311,
                    "type": "virtual",
                    "name": "signal-less-than",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1312817152
                  },
                  {
                    "index": 312,
                    "type": "virtual",
                    "name": "signal-greater-than",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1317011456
                  },
                  {
                    "index": 313,
                    "type": "virtual",
                    "name": "signal-less-than-or-equal-to",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1321205760
                  },
                  {
                    "index": 314,
                    "type": "virtual",
                    "name": "signal-greater-than-or-equal-to",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1325400064
                  },
                  {
                    "index": 315,
                    "type": "virtual",
                    "name": "signal-left-parenthesis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1329594368
                  },
                  {
                    "index": 316,
                    "type": "virtual",
                    "name": "signal-right-parenthesis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1333788672
                  },
                  {
                    "index": 317,
                    "type": "virtual",
                    "name": "signal-left-square-bracket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1337982976
                  },
                  {
                    "index": 318,
                    "type": "virtual",
                    "name": "signal-right-square-bracket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1342177280
                  },
                  {
                    "index": 319,
                    "type": "virtual",
                    "name": "signal-blue",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1354760192
                  },
                  {
                    "index": 320,
                    "type": "virtual",
                    "name": "signal-cyan",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1358954496
                  },
                  {
                    "index": 321,
                    "type": "virtual",
                    "name": "signal-pink",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1363148800
                  },
                  {
                    "index": 322,
                    "type": "virtual",
                    "name": "signal-yellow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1367343104
                  },
                  {
                    "index": 323,
                    "type": "virtual",
                    "name": "signal-white",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1371537408
                  },
                  {
                    "index": 324,
                    "type": "virtual",
                    "name": "signal-grey",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1375731712
                  },
                  {
                    "index": 325,
                    "type": "virtual",
                    "name": "signal-black",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1379926016
                  },
                  {
                    "index": 326,
                    "type": "virtual",
                    "name": "signal-check",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1384120320
                  },
                  {
                    "index": 327,
                    "type": "virtual",
                    "name": "signal-I",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1388314624
                  },
                  {
                    "index": 328,
                    "type": "virtual",
                    "name": "signal-no-entry",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1392508928
                  },
                  {
                    "index": 329,
                    "type": "virtual",
                    "name": "signal-heart",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1396703232
                  },
                  {
                    "index": 330,
                    "type": "virtual",
                    "name": "signal-alert",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1400897536
                  },
                  {
                    "index": 331,
                    "type": "virtual",
                    "name": "signal-star",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1405091840
                  },
                  {
                    "index": 332,
                    "type": "virtual",
                    "name": "signal-info",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1409286144
                  },
                  {
                    "index": 333,
                    "type": "virtual",
                    "name": "shape-vertical",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1413480448
                  },
                  {
                    "index": 334,
                    "type": "virtual",
                    "name": "shape-horizontal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1417674752
                  },
                  {
                    "index": 335,
                    "type": "virtual",
                    "name": "shape-curve",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1421869056
                  },
                  {
                    "index": 336,
                    "type": "virtual",
                    "name": "shape-curve-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1426063360
                  },
                  {
                    "index": 337,
                    "type": "virtual",
                    "name": "shape-corner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1430257664
                  },
                  {
                    "index": 338,
                    "type": "virtual",
                    "name": "shape-corner-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1434451968
                  },
                  {
                    "index": 339,
                    "type": "virtual",
                    "name": "shape-t",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1438646272
                  },
                  {
                    "index": 340,
                    "type": "virtual",
                    "name": "shape-t-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1442840576
                  },
                  {
                    "index": 341,
                    "type": "virtual",
                    "name": "shape-cross",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1447034880
                  },
                  {
                    "index": 342,
                    "type": "virtual",
                    "name": "shape-diagonal-cross",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1451229184
                  },
                  {
                    "index": 343,
                    "type": "virtual",
                    "name": "shape-diagonal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1455423488
                  },
                  {
                    "index": 344,
                    "type": "virtual",
                    "name": "shape-diagonal-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1459617792
                  },
                  {
                    "index": 345,
                    "type": "virtual",
                    "name": "shape-curve-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1463812096
                  },
                  {
                    "index": 346,
                    "type": "virtual",
                    "name": "shape-curve-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1468006400
                  },
                  {
                    "index": 347,
                    "type": "virtual",
                    "name": "shape-corner-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1472200704
                  },
                  {
                    "index": 348,
                    "type": "virtual",
                    "name": "shape-corner-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1476395008
                  },
                  {
                    "index": 349,
                    "type": "virtual",
                    "name": "shape-t-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1480589312
                  },
                  {
                    "index": 350,
                    "type": "virtual",
                    "name": "shape-t-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1484783616
                  },
                  {
                    "index": 351,
                    "name": "iron-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1488977920
                  },
                  {
                    "index": 352,
                    "name": "splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1493172224
                  },
                  {
                    "index": 353,
                    "type": "virtual",
                    "name": "up-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1497366528
                  },
                  {
                    "index": 354,
                    "type": "virtual",
                    "name": "up-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1501560832
                  },
                  {
                    "index": 355,
                    "type": "virtual",
                    "name": "right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1505755136
                  },
                  {
                    "index": 356,
                    "type": "virtual",
                    "name": "down-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1509949440
                  },
                  {
                    "index": 357,
                    "type": "virtual",
                    "name": "down-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1514143744
                  },
                  {
                    "index": 358,
                    "type": "virtual",
                    "name": "down-left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1518338048
                  },
                  {
                    "index": 359,
                    "type": "virtual",
                    "name": "left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1522532352
                  },
                  {
                    "index": 360,
                    "type": "virtual",
                    "name": "up-left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1526726656
                  },
                  {
                    "index": 361,
                    "type": "virtual",
                    "name": "signal-rightwards-leftwards-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1530920960
                  },
                  {
                    "index": 362,
                    "type": "virtual",
                    "name": "signal-upwards-downwards-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1535115264
                  },
                  {
                    "index": 363,
                    "type": "virtual",
                    "name": "signal-shuffle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1539309568
                  },
                  {
                    "index": 364,
                    "type": "virtual",
                    "name": "signal-left-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1543503872
                  },
                  {
                    "index": 365,
                    "type": "virtual",
                    "name": "signal-up-down-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1547698176
                  },
                  {
                    "index": 366,
                    "type": "virtual",
                    "name": "signal-clockwise-circle-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1551892480
                  },
                  {
                    "index": 367,
                    "type": "virtual",
                    "name": "signal-anticlockwise-circle-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1556086784
                  },
                  {
                    "index": 368,
                    "type": "virtual",
                    "name": "signal-input",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1560281088
                  },
                  {
                    "index": 369,
                    "type": "virtual",
                    "name": "signal-output",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1564475392
                  },
                  {
                    "index": 370,
                    "type": "virtual",
                    "name": "signal-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1568669696
                  },
                  {
                    "index": 371,
                    "type": "virtual",
                    "name": "signal-lightning",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1572864000
                  },
                  {
                    "index": 372,
                    "type": "virtual",
                    "name": "signal-battery-low",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1577058304
                  },
                  {
                    "index": 373,
                    "type": "virtual",
                    "name": "signal-battery-mid-level",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1581252608
                  },
                  {
                    "index": 374,
                    "type": "virtual",
                    "name": "signal-battery-full",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1585446912
                  },
                  {
                    "index": 375,
                    "type": "virtual",
                    "name": "signal-radioactivity",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1589641216
                  },
                  {
                    "index": 376,
                    "type": "virtual",
                    "name": "signal-thermometer-blue",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1593835520
                  },
                  {
                    "index": 377,
                    "type": "virtual",
                    "name": "signal-thermometer-red",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1598029824
                  },
                  {
                    "index": 378,
                    "type": "virtual",
                    "name": "signal-fire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1602224128
                  },
                  {
                    "index": 379,
                    "type": "virtual",
                    "name": "signal-snowflake",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1606418432
                  },
                  {
                    "index": 380,
                    "type": "virtual",
                    "name": "signal-explosion",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1610612736
                  },
                  {
                    "index": 381,
                    "type": "virtual",
                    "name": "signal-liquid",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1614807040
                  },
                  {
                    "index": 382,
                    "type": "virtual",
                    "name": "signal-stack-size",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1619001344
                  },
                  {
                    "index": 383,
                    "type": "virtual",
                    "name": "signal-recycle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1623195648
                  },
                  {
                    "index": 384,
                    "type": "virtual",
                    "name": "signal-trash-bin",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1627389952
                  },
                  {
                    "index": 385,
                    "type": "virtual",
                    "name": "signal-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1631584256
                  },
                  {
                    "index": 386,
                    "type": "virtual",
                    "name": "signal-map-marker",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1635778560
                  },
                  {
                    "index": 387,
                    "type": "virtual",
                    "name": "signal-white-flag",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1639972864
                  },
                  {
                    "index": 388,
                    "type": "virtual",
                    "name": "signal-lock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1644167168
                  },
                  {
                    "index": 389,
                    "type": "virtual",
                    "name": "signal-unlock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1648361472
                  },
                  {
                    "index": 390,
                    "type": "virtual",
                    "name": "signal-speed",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1652555776
                  },
                  {
                    "index": 391,
                    "type": "virtual",
                    "name": "signal-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1656750080
                  },
                  {
                    "index": 392,
                    "type": "virtual",
                    "name": "signal-hourglass",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1660944384
                  },
                  {
                    "index": 393,
                    "type": "virtual",
                    "name": "signal-alarm",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1665138688
                  },
                  {
                    "index": 394,
                    "type": "virtual",
                    "name": "signal-sun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1669332992
                  },
                  {
                    "index": 395,
                    "type": "virtual",
                    "name": "signal-moon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1673527296
                  },
                  {
                    "index": 396,
                    "type": "virtual",
                    "name": "signal-mining",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1677721600
                  },
                  {
                    "index": 397,
                    "type": "virtual",
                    "name": "signal-skull",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1681915904
                  },
                  {
                    "index": 398,
                    "type": "virtual",
                    "name": "signal-damage",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1686110208
                  },
                  {
                    "index": 399,
                    "type": "virtual",
                    "name": "signal-weapon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1690304512
                  }
                ]
              }
            ]
          }
        }
      },
      {
        "entity_number": 3,
        "name": "constant-combinator",
        "position": {
          "x": 562.5,
          "y": -22.5
        },
        "direction": 4,
        "control_behavior": {
          "sections": {
            "sections": [
              {
                "index": 1,
                "filters": [
                  {
                    "index": 1,
                    "type": "virtual",
                    "name": "signal-deny",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 4194304
                  },
                  {
                    "index": 2,
                    "type": "virtual",
                    "name": "signal-0",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 8388608
                  },
                  {
                    "index": 3,
                    "type": "virtual",
                    "name": "signal-1",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 12582912
                  },
                  {
                    "index": 4,
                    "type": "virtual",
                    "name": "signal-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 16777216
                  },
                  {
                    "index": 5,
                    "type": "virtual",
                    "name": "signal-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 20971520
                  },
                  {
                    "index": 6,
                    "type": "virtual",
                    "name": "signal-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 25165824
                  },
                  {
                    "index": 7,
                    "type": "virtual",
                    "name": "signal-5",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 29360128
                  },
                  {
                    "index": 8,
                    "type": "virtual",
                    "name": "signal-6",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 33554432
                  },
                  {
                    "index": 9,
                    "type": "virtual",
                    "name": "signal-7",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 37748736
                  },
                  {
                    "index": 10,
                    "type": "virtual",
                    "name": "signal-8",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 41943040
                  },
                  {
                    "index": 11,
                    "type": "virtual",
                    "name": "signal-9",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 46137344
                  },
                  {
                    "index": 12,
                    "type": "virtual",
                    "name": "signal-dot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 50331648
                  },
                  {
                    "index": 13,
                    "type": "virtual",
                    "name": "shape-circle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 54525952
                  },
                  {
                    "index": 14,
                    "name": "burner-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 58720256
                  },
                  {
                    "index": 15,
                    "name": "inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 62914560
                  },
                  {
                    "index": 16,
                    "name": "long-handed-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 67108864
                  },
                  {
                    "index": 17,
                    "name": "fast-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 71303168
                  },
                  {
                    "index": 18,
                    "name": "bulk-inserter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 75497472
                  },
                  {
                    "index": 19,
                    "name": "small-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 79691776
                  },
                  {
                    "index": 20,
                    "name": "medium-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 83886080
                  },
                  {
                    "index": 21,
                    "name": "big-electric-pole",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 88080384
                  },
                  {
                    "index": 22,
                    "name": "substation",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 92274688
                  },
                  {
                    "index": 23,
                    "name": "pipe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 96468992
                  },
                  {
                    "index": 24,
                    "name": "pipe-to-ground",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 100663296
                  },
                  {
                    "index": 25,
                    "name": "pump",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 104857600
                  },
                  {
                    "index": 26,
                    "name": "rail",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 109051904
                  },
                  {
                    "index": 27,
                    "name": "train-stop",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 113246208
                  },
                  {
                    "index": 28,
                    "name": "rail-signal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 117440512
                  },
                  {
                    "index": 29,
                    "name": "rail-chain-signal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 121634816
                  },
                  {
                    "index": 30,
                    "name": "locomotive",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 125829120
                  },
                  {
                    "index": 31,
                    "name": "cargo-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 130023424
                  },
                  {
                    "index": 32,
                    "name": "fluid-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 134217728
                  },
                  {
                    "index": 33,
                    "name": "artillery-wagon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 138412032
                  },
                  {
                    "index": 34,
                    "name": "car",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 142606336
                  },
                  {
                    "index": 35,
                    "name": "tank",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 146800640
                  },
                  {
                    "index": 36,
                    "name": "spidertron",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 150994944
                  },
                  {
                    "index": 37,
                    "name": "underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 155189248
                  },
                  {
                    "index": 38,
                    "name": "construction-robot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 159383552
                  },
                  {
                    "index": 39,
                    "name": "active-provider-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 163577856
                  },
                  {
                    "index": 40,
                    "name": "passive-provider-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 167772160
                  },
                  {
                    "index": 41,
                    "name": "small-lamp",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 171966464
                  },
                  {
                    "index": 42,
                    "name": "arithmetic-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 176160768
                  },
                  {
                    "index": 43,
                    "name": "fast-splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 180355072
                  },
                  {
                    "index": 44,
                    "name": "selector-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 184549376
                  },
                  {
                    "index": 45,
                    "name": "storage-tank",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 188743680
                  },
                  {
                    "index": 46,
                    "name": "express-transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 192937984
                  },
                  {
                    "index": 47,
                    "name": "programmable-speaker",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 197132288
                  },
                  {
                    "index": 48,
                    "name": "display-panel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 201326592
                  },
                  {
                    "index": 49,
                    "name": "stone-brick",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 205520896
                  },
                  {
                    "index": 50,
                    "name": "concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 209715200
                  },
                  {
                    "index": 51,
                    "name": "hazard-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 213909504
                  },
                  {
                    "index": 52,
                    "name": "refined-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 218103808
                  },
                  {
                    "index": 53,
                    "name": "refined-hazard-concrete",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 222298112
                  },
                  {
                    "index": 54,
                    "name": "landfill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 226492416
                  },
                  {
                    "index": 55,
                    "name": "cliff-explosives",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 230686720,
                    "import_from": "nauvis"
                  },
                  {
                    "index": 56,
                    "name": "repair-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 234881024
                  },
                  {
                    "index": 57,
                    "name": "blueprint",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 239075328
                  },
                  {
                    "index": 58,
                    "name": "deconstruction-planner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 243269632
                  },
                  {
                    "index": 59,
                    "name": "upgrade-planner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 247463936
                  },
                  {
                    "index": 60,
                    "name": "blueprint-book",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 251658240
                  },
                  {
                    "index": 61,
                    "name": "boiler",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 255852544
                  },
                  {
                    "index": 62,
                    "name": "steam-engine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 260046848
                  },
                  {
                    "index": 63,
                    "name": "solar-panel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 264241152
                  },
                  {
                    "index": 64,
                    "name": "accumulator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 268435456
                  },
                  {
                    "index": 65,
                    "name": "nuclear-reactor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 272629760
                  },
                  {
                    "index": 66,
                    "name": "express-underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 276824064
                  },
                  {
                    "index": 67,
                    "name": "heat-exchanger",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 281018368
                  },
                  {
                    "index": 68,
                    "name": "steam-turbine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 285212672
                  },
                  {
                    "index": 69,
                    "name": "burner-mining-drill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 289406976
                  },
                  {
                    "index": 70,
                    "name": "electric-mining-drill",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 293601280
                  },
                  {
                    "index": 71,
                    "name": "offshore-pump",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 297795584
                  },
                  {
                    "index": 72,
                    "name": "pumpjack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 301989888
                  },
                  {
                    "index": 73,
                    "name": "stone-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 306184192
                  },
                  {
                    "index": 74,
                    "name": "steel-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 310378496
                  },
                  {
                    "index": 75,
                    "name": "electric-furnace",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 314572800
                  },
                  {
                    "index": 76,
                    "name": "fast-underground-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 318767104
                  },
                  {
                    "index": 77,
                    "name": "assembling-machine-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 322961408
                  },
                  {
                    "index": 78,
                    "name": "assembling-machine-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 327155712
                  },
                  {
                    "index": 79,
                    "name": "oil-refinery",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 331350016
                  },
                  {
                    "index": 80,
                    "name": "chemical-plant",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 335544320
                  },
                  {
                    "index": 81,
                    "name": "centrifuge",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 339738624
                  },
                  {
                    "index": 82,
                    "name": "lab",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 343932928
                  },
                  {
                    "index": 83,
                    "name": "wooden-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 348127232
                  },
                  {
                    "index": 84,
                    "name": "speed-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 352321536
                  },
                  {
                    "index": 85,
                    "name": "speed-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 356515840
                  },
                  {
                    "index": 86,
                    "name": "speed-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 360710144
                  },
                  {
                    "index": 87,
                    "name": "efficiency-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 364904448
                  },
                  {
                    "index": 88,
                    "name": "efficiency-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 369098752
                  },
                  {
                    "index": 89,
                    "name": "efficiency-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 373293056
                  },
                  {
                    "index": 90,
                    "name": "productivity-module",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 377487360
                  },
                  {
                    "index": 91,
                    "name": "productivity-module-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 381681664
                  },
                  {
                    "index": 92,
                    "name": "productivity-module-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 385875968
                  },
                  {
                    "index": 93,
                    "name": "rocket-silo",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 390070272
                  },
                  {
                    "index": 94,
                    "name": "cargo-landing-pad",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 394264576
                  },
                  {
                    "index": 95,
                    "name": "steel-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 398458880
                  },
                  {
                    "index": 96,
                    "type": "recipe",
                    "name": "basic-oil-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 402653184
                  },
                  {
                    "index": 97,
                    "name": "logistic-robot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 406847488
                  },
                  {
                    "index": 98,
                    "type": "recipe",
                    "name": "coal-liquefaction",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 411041792
                  },
                  {
                    "index": 99,
                    "type": "recipe",
                    "name": "heavy-oil-cracking",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 415236096
                  },
                  {
                    "index": 100,
                    "type": "recipe",
                    "name": "light-oil-cracking",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 419430400
                  },
                  {
                    "index": 101,
                    "type": "recipe",
                    "name": "solid-fuel-from-petroleum-gas",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 423624704
                  },
                  {
                    "index": 102,
                    "type": "recipe",
                    "name": "solid-fuel-from-light-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 427819008
                  },
                  {
                    "index": 103,
                    "type": "recipe",
                    "name": "solid-fuel-from-heavy-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 432013312
                  },
                  {
                    "index": 104,
                    "name": "express-splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 436207616
                  },
                  {
                    "index": 105,
                    "name": "coal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 440401920
                  },
                  {
                    "index": 106,
                    "name": "stone",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 444596224
                  },
                  {
                    "index": 107,
                    "name": "iron-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 448790528
                  },
                  {
                    "index": 108,
                    "name": "copper-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 452984832
                  },
                  {
                    "index": 109,
                    "name": "uranium-ore",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 457179136
                  },
                  {
                    "index": 110,
                    "name": "raw-fish",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 461373440
                  },
                  {
                    "index": 111,
                    "name": "iron-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 465567744
                  },
                  {
                    "index": 112,
                    "name": "copper-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 469762048
                  },
                  {
                    "index": 113,
                    "name": "steel-plate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 473956352
                  },
                  {
                    "index": 114,
                    "name": "solid-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 478150656
                  },
                  {
                    "index": 115,
                    "name": "plastic-bar",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 482344960
                  },
                  {
                    "index": 116,
                    "name": "sulfur",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 486539264
                  },
                  {
                    "index": 117,
                    "name": "battery",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 490733568
                  },
                  {
                    "index": 118,
                    "name": "explosives",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 494927872
                  },
                  {
                    "index": 119,
                    "name": "water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 499122176
                  },
                  {
                    "index": 120,
                    "name": "crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 503316480
                  },
                  {
                    "index": 121,
                    "name": "petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 507510784
                  },
                  {
                    "index": 122,
                    "name": "light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 511705088
                  },
                  {
                    "index": 123,
                    "name": "decider-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 515899392
                  },
                  {
                    "index": 124,
                    "name": "lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 520093696
                  },
                  {
                    "index": 125,
                    "name": "sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 524288000
                  },
                  {
                    "index": 126,
                    "name": "power-switch",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 528482304
                  },
                  {
                    "index": 127,
                    "type": "recipe",
                    "name": "crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 532676608
                  },
                  {
                    "index": 128,
                    "type": "recipe",
                    "name": "petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 536870912
                  },
                  {
                    "index": 129,
                    "type": "recipe",
                    "name": "light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 541065216
                  },
                  {
                    "index": 130,
                    "type": "recipe",
                    "name": "heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 545259520
                  },
                  {
                    "index": 131,
                    "type": "recipe",
                    "name": "lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 549453824
                  },
                  {
                    "index": 132,
                    "type": "recipe",
                    "name": "sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 553648128
                  },
                  {
                    "index": 133,
                    "type": "recipe",
                    "name": "empty-water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 557842432
                  },
                  {
                    "index": 134,
                    "type": "recipe",
                    "name": "empty-crude-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 562036736
                  },
                  {
                    "index": 135,
                    "type": "recipe",
                    "name": "empty-petroleum-gas-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 566231040
                  },
                  {
                    "index": 136,
                    "type": "recipe",
                    "name": "empty-light-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 570425344
                  },
                  {
                    "index": 137,
                    "type": "recipe",
                    "name": "empty-heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 574619648
                  },
                  {
                    "index": 138,
                    "type": "recipe",
                    "name": "empty-lubricant-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 578813952
                  },
                  {
                    "index": 139,
                    "type": "recipe",
                    "name": "empty-sulfuric-acid-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 583008256
                  },
                  {
                    "index": 140,
                    "name": "iron-gear-wheel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 587202560
                  },
                  {
                    "index": 141,
                    "name": "iron-stick",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 591396864
                  },
                  {
                    "index": 142,
                    "name": "copper-cable",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 595591168
                  },
                  {
                    "index": 143,
                    "name": "barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 599785472
                  },
                  {
                    "index": 144,
                    "name": "constant-combinator",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 603979776
                  },
                  {
                    "index": 145,
                    "name": "advanced-circuit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 608174080
                  },
                  {
                    "index": 146,
                    "name": "processing-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 612368384
                  },
                  {
                    "index": 147,
                    "name": "engine-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 616562688
                  },
                  {
                    "index": 148,
                    "name": "electric-engine-unit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 620756992
                  },
                  {
                    "index": 149,
                    "name": "flying-robot-frame",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 624951296
                  },
                  {
                    "index": 150,
                    "name": "low-density-structure",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 629145600
                  },
                  {
                    "index": 151,
                    "name": "rocket-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 633339904
                  },
                  {
                    "index": 152,
                    "type": "recipe",
                    "name": "rocket-part",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 637534208
                  },
                  {
                    "index": 153,
                    "type": "recipe",
                    "name": "uranium-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 641728512
                  },
                  {
                    "index": 154,
                    "name": "uranium-235",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 645922816
                  },
                  {
                    "index": 155,
                    "name": "uranium-238",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 650117120
                  },
                  {
                    "index": 156,
                    "name": "uranium-fuel-cell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 654311424
                  },
                  {
                    "index": 157,
                    "name": "depleted-uranium-fuel-cell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 658505728
                  },
                  {
                    "index": 158,
                    "type": "recipe",
                    "name": "nuclear-fuel-reprocessing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 662700032
                  },
                  {
                    "index": 159,
                    "type": "recipe",
                    "name": "kovarex-enrichment-process",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 666894336
                  },
                  {
                    "index": 160,
                    "name": "nuclear-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 671088640
                  },
                  {
                    "index": 161,
                    "name": "automation-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 675282944
                  },
                  {
                    "index": 162,
                    "name": "logistic-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 679477248
                  },
                  {
                    "index": 163,
                    "name": "military-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 683671552
                  },
                  {
                    "index": 164,
                    "name": "beacon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 687865856
                  },
                  {
                    "index": 165,
                    "name": "production-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 692060160
                  },
                  {
                    "index": 166,
                    "name": "utility-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 696254464
                  },
                  {
                    "index": 167,
                    "name": "space-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 700448768
                  },
                  {
                    "index": 168,
                    "name": "pistol",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 704643072
                  },
                  {
                    "index": 169,
                    "name": "submachine-gun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 708837376
                  },
                  {
                    "index": 170,
                    "name": "shotgun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 713031680
                  },
                  {
                    "index": 171,
                    "name": "combat-shotgun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 717225984
                  },
                  {
                    "index": 172,
                    "name": "rocket-launcher",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 721420288
                  },
                  {
                    "index": 173,
                    "name": "flamethrower",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 725614592
                  },
                  {
                    "index": 174,
                    "name": "firearm-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 729808896
                  },
                  {
                    "index": 175,
                    "name": "piercing-rounds-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 734003200
                  },
                  {
                    "index": 176,
                    "name": "uranium-rounds-magazine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 738197504
                  },
                  {
                    "index": 177,
                    "type": "recipe",
                    "name": "advanced-oil-processing",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 742391808
                  },
                  {
                    "index": 178,
                    "name": "piercing-shotgun-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 746586112
                  },
                  {
                    "index": 179,
                    "name": "cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 750780416
                  },
                  {
                    "index": 180,
                    "name": "explosive-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 754974720
                  },
                  {
                    "index": 181,
                    "name": "uranium-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 759169024
                  },
                  {
                    "index": 182,
                    "name": "explosive-uranium-cannon-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 763363328
                  },
                  {
                    "index": 183,
                    "name": "artillery-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 767557632
                  },
                  {
                    "index": 184,
                    "name": "rocket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 771751936
                  },
                  {
                    "index": 185,
                    "name": "assembling-machine-1",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 775946240
                  },
                  {
                    "index": 186,
                    "name": "flamethrower-ammo",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 780140544
                  },
                  {
                    "index": 187,
                    "name": "grenade",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 784334848
                  },
                  {
                    "index": 188,
                    "name": "cluster-grenade",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 788529152
                  },
                  {
                    "index": 189,
                    "name": "poison-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 792723456
                  },
                  {
                    "index": 190,
                    "name": "slowdown-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 796917760
                  },
                  {
                    "index": 191,
                    "name": "defender-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 801112064
                  },
                  {
                    "index": 192,
                    "type": "entity",
                    "name": "defender",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 805306368
                  },
                  {
                    "index": 193,
                    "type": "entity",
                    "name": "distractor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 809500672
                  },
                  {
                    "index": 194,
                    "name": "wood",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 813694976
                  },
                  {
                    "index": 195,
                    "name": "fast-transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 817889280
                  },
                  {
                    "index": 196,
                    "name": "destroyer-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 822083584
                  },
                  {
                    "index": 197,
                    "name": "light-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 826277888
                  },
                  {
                    "index": 198,
                    "name": "heavy-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 830472192
                  },
                  {
                    "index": 199,
                    "name": "modular-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 834666496
                  },
                  {
                    "index": 200,
                    "name": "power-armor",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 838860800
                  },
                  {
                    "index": 201,
                    "name": "power-armor-mk2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 843055104
                  },
                  {
                    "index": 202,
                    "name": "heavy-oil-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 847249408
                  },
                  {
                    "index": 203,
                    "name": "fission-reactor-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 851443712
                  },
                  {
                    "index": 204,
                    "name": "battery-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 855638016
                  },
                  {
                    "index": 205,
                    "name": "transport-belt",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 859832320
                  },
                  {
                    "index": 206,
                    "type": "recipe",
                    "name": "water-barrel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 864026624
                  },
                  {
                    "index": 207,
                    "name": "exoskeleton-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 868220928
                  },
                  {
                    "index": 208,
                    "name": "personal-roboport-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 872415232
                  },
                  {
                    "index": 209,
                    "name": "personal-roboport-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 876609536
                  },
                  {
                    "index": 210,
                    "name": "night-vision-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 880803840
                  },
                  {
                    "index": 211,
                    "name": "energy-shield-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 884998144
                  },
                  {
                    "index": 212,
                    "name": "energy-shield-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 889192448
                  },
                  {
                    "index": 213,
                    "name": "personal-laser-defense-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 893386752
                  },
                  {
                    "index": 214,
                    "name": "discharge-defense-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 897581056
                  },
                  {
                    "index": 215,
                    "name": "stone-wall",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 901775360
                  },
                  {
                    "index": 216,
                    "name": "gate",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 905969664
                  },
                  {
                    "index": 217,
                    "name": "radar",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 910163968
                  },
                  {
                    "index": 218,
                    "name": "land-mine",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 914358272
                  },
                  {
                    "index": 219,
                    "name": "gun-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 918552576
                  },
                  {
                    "index": 220,
                    "name": "laser-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 922746880
                  },
                  {
                    "index": 221,
                    "name": "flamethrower-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 926941184
                  },
                  {
                    "index": 222,
                    "name": "artillery-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 931135488
                  },
                  {
                    "index": 223,
                    "type": "fluid",
                    "name": "water",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 935329792
                  },
                  {
                    "index": 224,
                    "type": "fluid",
                    "name": "steam",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 939524096
                  },
                  {
                    "index": 225,
                    "type": "fluid",
                    "name": "crude-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 943718400
                  },
                  {
                    "index": 226,
                    "type": "fluid",
                    "name": "petroleum-gas",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 947912704
                  },
                  {
                    "index": 227,
                    "type": "fluid",
                    "name": "light-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 952107008
                  },
                  {
                    "index": 228,
                    "type": "fluid",
                    "name": "heavy-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 956301312
                  },
                  {
                    "index": 229,
                    "type": "fluid",
                    "name": "lubricant",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 960495616
                  },
                  {
                    "index": 230,
                    "type": "fluid",
                    "name": "sulfuric-acid",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 964689920
                  },
                  {
                    "index": 231,
                    "type": "entity",
                    "name": "small-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 968884224
                  },
                  {
                    "index": 232,
                    "type": "entity",
                    "name": "medium-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 973078528
                  },
                  {
                    "index": 233,
                    "type": "entity",
                    "name": "big-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 977272832
                  },
                  {
                    "index": 234,
                    "type": "entity",
                    "name": "behemoth-biter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 981467136
                  },
                  {
                    "index": 235,
                    "type": "entity",
                    "name": "small-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 985661440
                  },
                  {
                    "index": 236,
                    "type": "entity",
                    "name": "medium-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 989855744
                  },
                  {
                    "index": 237,
                    "type": "entity",
                    "name": "big-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 994050048
                  },
                  {
                    "index": 238,
                    "type": "entity",
                    "name": "behemoth-spitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 998244352
                  },
                  {
                    "index": 239,
                    "type": "entity",
                    "name": "small-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1002438656
                  },
                  {
                    "index": 240,
                    "type": "entity",
                    "name": "medium-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1006632960
                  },
                  {
                    "index": 241,
                    "type": "entity",
                    "name": "big-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1010827264
                  },
                  {
                    "index": 242,
                    "type": "entity",
                    "name": "behemoth-worm-turret",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1015021568
                  },
                  {
                    "index": 243,
                    "type": "entity",
                    "name": "biter-spawner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1019215872
                  },
                  {
                    "index": 244,
                    "type": "entity",
                    "name": "spitter-spawner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1023410176
                  },
                  {
                    "index": 245,
                    "type": "entity",
                    "name": "cliff",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1027604480
                  },
                  {
                    "index": 246,
                    "type": "entity",
                    "name": "character",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1031798784
                  },
                  {
                    "index": 247,
                    "type": "entity",
                    "name": "big-sand-rock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1035993088
                  },
                  {
                    "index": 248,
                    "type": "entity",
                    "name": "huge-rock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1040187392
                  },
                  {
                    "index": 249,
                    "type": "entity",
                    "name": "crude-oil",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1044381696
                  },
                  {
                    "index": 250,
                    "name": "copper-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1048576000
                  },
                  {
                    "index": 251,
                    "name": "green-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1052770304
                  },
                  {
                    "index": 252,
                    "name": "red-wire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1056964608
                  },
                  {
                    "index": 253,
                    "name": "spidertron-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1061158912
                  },
                  {
                    "index": 254,
                    "name": "discharge-defense-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1065353216
                  },
                  {
                    "index": 255,
                    "name": "artillery-targeting-remote",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1069547520
                  },
                  {
                    "index": 256,
                    "type": "entity",
                    "name": "entity-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1073741824
                  },
                  {
                    "index": 257,
                    "type": "entity",
                    "name": "item-on-ground",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1077936128
                  },
                  {
                    "index": 258,
                    "type": "entity",
                    "name": "item-request-proxy",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1082130432
                  },
                  {
                    "index": 259,
                    "type": "entity",
                    "name": "tile-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1086324736
                  },
                  {
                    "index": 260,
                    "type": "space-location",
                    "name": "nauvis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1090519040
                  },
                  {
                    "index": 261,
                    "type": "entity",
                    "name": "cargo-pod",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1094713344
                  },
                  {
                    "index": 262,
                    "type": "entity",
                    "name": "cargo-pod-container",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1098907648
                  },
                  {
                    "index": 263,
                    "name": "chemical-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1103101952
                  },
                  {
                    "index": 264,
                    "type": "entity",
                    "name": "destroyer",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1107296256
                  },
                  {
                    "index": 265,
                    "name": "explosive-rocket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1111490560
                  },
                  {
                    "index": 266,
                    "name": "electronic-circuit",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1115684864
                  },
                  {
                    "index": 267,
                    "name": "belt-immunity-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1119879168
                  },
                  {
                    "index": 268,
                    "name": "shotgun-shell",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1124073472
                  },
                  {
                    "index": 269,
                    "name": "battery-mk2-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1128267776
                  },
                  {
                    "index": 270,
                    "name": "heat-pipe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1132462080
                  },
                  {
                    "index": 271,
                    "name": "atomic-bomb",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1136656384
                  },
                  {
                    "index": 272,
                    "name": "distractor-capsule",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1140850688
                  },
                  {
                    "index": 273,
                    "type": "virtual",
                    "name": "signal-A",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1145044992
                  },
                  {
                    "index": 274,
                    "type": "virtual",
                    "name": "signal-B",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1149239296
                  },
                  {
                    "index": 275,
                    "type": "virtual",
                    "name": "signal-D",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1157627904
                  },
                  {
                    "index": 276,
                    "type": "virtual",
                    "name": "signal-E",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1161822208
                  },
                  {
                    "index": 277,
                    "type": "virtual",
                    "name": "signal-F",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1166016512
                  },
                  {
                    "index": 278,
                    "type": "virtual",
                    "name": "signal-G",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1170210816
                  },
                  {
                    "index": 279,
                    "type": "virtual",
                    "name": "signal-H",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1174405120
                  },
                  {
                    "index": 280,
                    "name": "solar-panel-equipment",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1178599424
                  },
                  {
                    "index": 281,
                    "type": "virtual",
                    "name": "signal-J",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1182793728
                  },
                  {
                    "index": 282,
                    "type": "virtual",
                    "name": "signal-K",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1186988032
                  },
                  {
                    "index": 283,
                    "type": "virtual",
                    "name": "signal-L",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1191182336
                  },
                  {
                    "index": 284,
                    "type": "virtual",
                    "name": "signal-M",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1195376640
                  },
                  {
                    "index": 285,
                    "type": "virtual",
                    "name": "signal-N",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1199570944
                  },
                  {
                    "index": 286,
                    "type": "virtual",
                    "name": "signal-O",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1203765248
                  },
                  {
                    "index": 287,
                    "type": "virtual",
                    "name": "signal-P",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1207959552
                  },
                  {
                    "index": 288,
                    "type": "virtual",
                    "name": "signal-Q",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1212153856
                  },
                  {
                    "index": 289,
                    "type": "virtual",
                    "name": "signal-R",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1216348160
                  },
                  {
                    "index": 290,
                    "type": "virtual",
                    "name": "signal-T",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1224736768
                  },
                  {
                    "index": 291,
                    "type": "virtual",
                    "name": "signal-U",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1228931072
                  },
                  {
                    "index": 292,
                    "type": "virtual",
                    "name": "signal-V",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1233125376
                  },
                  {
                    "index": 293,
                    "type": "virtual",
                    "name": "signal-W",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1237319680
                  },
                  {
                    "index": 294,
                    "type": "virtual",
                    "name": "signal-X",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1241513984
                  },
                  {
                    "index": 295,
                    "type": "virtual",
                    "name": "signal-Y",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1245708288
                  },
                  {
                    "index": 296,
                    "type": "virtual",
                    "name": "signal-Z",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1249902592
                  },
                  {
                    "index": 297,
                    "type": "virtual",
                    "name": "signal-comma",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1254096896
                  },
                  {
                    "index": 298,
                    "type": "virtual",
                    "name": "signal-letter-dot",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1258291200
                  },
                  {
                    "index": 299,
                    "type": "virtual",
                    "name": "signal-exclamation-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1262485504
                  },
                  {
                    "index": 300,
                    "type": "virtual",
                    "name": "signal-question-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1266679808
                  },
                  {
                    "index": 301,
                    "type": "virtual",
                    "name": "signal-colon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1270874112
                  },
                  {
                    "index": 302,
                    "type": "virtual",
                    "name": "signal-apostrophe",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1275068416
                  },
                  {
                    "index": 303,
                    "type": "virtual",
                    "name": "signal-quotation-mark",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1279262720
                  },
                  {
                    "index": 304,
                    "type": "virtual",
                    "name": "signal-ampersand",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1283457024
                  },
                  {
                    "index": 305,
                    "type": "virtual",
                    "name": "signal-circumflex-accent",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1287651328
                  },
                  {
                    "index": 306,
                    "type": "virtual",
                    "name": "signal-number-sign",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1291845632
                  },
                  {
                    "index": 307,
                    "type": "virtual",
                    "name": "signal-multiplication",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1296039936
                  },
                  {
                    "index": 308,
                    "type": "virtual",
                    "name": "signal-division",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1300234240
                  },
                  {
                    "index": 309,
                    "type": "virtual",
                    "name": "signal-equal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1304428544
                  },
                  {
                    "index": 310,
                    "type": "virtual",
                    "name": "signal-not-equal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1308622848
                  },
                  {
                    "index": 311,
                    "type": "virtual",
                    "name": "signal-less-than",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1312817152
                  },
                  {
                    "index": 312,
                    "type": "virtual",
                    "name": "signal-greater-than",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1317011456
                  },
                  {
                    "index": 313,
                    "type": "virtual",
                    "name": "signal-less-than-or-equal-to",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1321205760
                  },
                  {
                    "index": 314,
                    "type": "virtual",
                    "name": "signal-greater-than-or-equal-to",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1325400064
                  },
                  {
                    "index": 315,
                    "type": "virtual",
                    "name": "signal-left-parenthesis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1329594368
                  },
                  {
                    "index": 316,
                    "type": "virtual",
                    "name": "signal-right-parenthesis",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1333788672
                  },
                  {
                    "index": 317,
                    "type": "virtual",
                    "name": "signal-left-square-bracket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1337982976
                  },
                  {
                    "index": 318,
                    "type": "virtual",
                    "name": "signal-right-square-bracket",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1342177280
                  },
                  {
                    "index": 319,
                    "type": "virtual",
                    "name": "signal-blue",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1354760192
                  },
                  {
                    "index": 320,
                    "type": "virtual",
                    "name": "signal-cyan",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1358954496
                  },
                  {
                    "index": 321,
                    "type": "virtual",
                    "name": "signal-pink",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1363148800
                  },
                  {
                    "index": 322,
                    "type": "virtual",
                    "name": "signal-yellow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1367343104
                  },
                  {
                    "index": 323,
                    "type": "virtual",
                    "name": "signal-white",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1371537408
                  },
                  {
                    "index": 324,
                    "type": "virtual",
                    "name": "signal-grey",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1375731712
                  },
                  {
                    "index": 325,
                    "type": "virtual",
                    "name": "signal-black",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1379926016
                  },
                  {
                    "index": 326,
                    "type": "virtual",
                    "name": "signal-check",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1384120320
                  },
                  {
                    "index": 327,
                    "type": "virtual",
                    "name": "signal-I",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1388314624
                  },
                  {
                    "index": 328,
                    "type": "virtual",
                    "name": "signal-no-entry",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1392508928
                  },
                  {
                    "index": 329,
                    "type": "virtual",
                    "name": "signal-heart",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1396703232
                  },
                  {
                    "index": 330,
                    "type": "virtual",
                    "name": "signal-alert",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1400897536
                  },
                  {
                    "index": 331,
                    "type": "virtual",
                    "name": "signal-star",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1405091840
                  },
                  {
                    "index": 332,
                    "type": "virtual",
                    "name": "signal-info",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1409286144
                  },
                  {
                    "index": 333,
                    "type": "virtual",
                    "name": "shape-vertical",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1413480448
                  },
                  {
                    "index": 334,
                    "type": "virtual",
                    "name": "shape-horizontal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1417674752
                  },
                  {
                    "index": 335,
                    "type": "virtual",
                    "name": "shape-curve",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1421869056
                  },
                  {
                    "index": 336,
                    "type": "virtual",
                    "name": "shape-curve-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1426063360
                  },
                  {
                    "index": 337,
                    "type": "virtual",
                    "name": "shape-corner",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1430257664
                  },
                  {
                    "index": 338,
                    "type": "virtual",
                    "name": "shape-corner-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1434451968
                  },
                  {
                    "index": 339,
                    "type": "virtual",
                    "name": "shape-t",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1438646272
                  },
                  {
                    "index": 340,
                    "type": "virtual",
                    "name": "shape-t-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1442840576
                  },
                  {
                    "index": 341,
                    "type": "virtual",
                    "name": "shape-cross",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1447034880
                  },
                  {
                    "index": 342,
                    "type": "virtual",
                    "name": "shape-diagonal-cross",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1451229184
                  },
                  {
                    "index": 343,
                    "type": "virtual",
                    "name": "shape-diagonal",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1455423488
                  },
                  {
                    "index": 344,
                    "type": "virtual",
                    "name": "shape-diagonal-2",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1459617792
                  },
                  {
                    "index": 345,
                    "type": "virtual",
                    "name": "shape-curve-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1463812096
                  },
                  {
                    "index": 346,
                    "type": "virtual",
                    "name": "shape-curve-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1468006400
                  },
                  {
                    "index": 347,
                    "type": "virtual",
                    "name": "shape-corner-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1472200704
                  },
                  {
                    "index": 348,
                    "type": "virtual",
                    "name": "shape-corner-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1476395008
                  },
                  {
                    "index": 349,
                    "type": "virtual",
                    "name": "shape-t-4",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1480589312
                  },
                  {
                    "index": 350,
                    "type": "virtual",
                    "name": "shape-t-3",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1484783616
                  },
                  {
                    "index": 351,
                    "name": "iron-chest",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1488977920
                  },
                  {
                    "index": 352,
                    "name": "splitter",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1493172224
                  },
                  {
                    "index": 353,
                    "type": "virtual",
                    "name": "up-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1497366528
                  },
                  {
                    "index": 354,
                    "type": "virtual",
                    "name": "up-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1501560832
                  },
                  {
                    "index": 355,
                    "type": "virtual",
                    "name": "right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1505755136
                  },
                  {
                    "index": 356,
                    "type": "virtual",
                    "name": "down-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1509949440
                  },
                  {
                    "index": 357,
                    "type": "virtual",
                    "name": "down-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1514143744
                  },
                  {
                    "index": 358,
                    "type": "virtual",
                    "name": "down-left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1518338048
                  },
                  {
                    "index": 359,
                    "type": "virtual",
                    "name": "left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1522532352
                  },
                  {
                    "index": 360,
                    "type": "virtual",
                    "name": "up-left-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1526726656
                  },
                  {
                    "index": 361,
                    "type": "virtual",
                    "name": "signal-rightwards-leftwards-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1530920960
                  },
                  {
                    "index": 362,
                    "type": "virtual",
                    "name": "signal-upwards-downwards-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1535115264
                  },
                  {
                    "index": 363,
                    "type": "virtual",
                    "name": "signal-shuffle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1539309568
                  },
                  {
                    "index": 364,
                    "type": "virtual",
                    "name": "signal-left-right-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1543503872
                  },
                  {
                    "index": 365,
                    "type": "virtual",
                    "name": "signal-up-down-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1547698176
                  },
                  {
                    "index": 366,
                    "type": "virtual",
                    "name": "signal-clockwise-circle-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1551892480
                  },
                  {
                    "index": 367,
                    "type": "virtual",
                    "name": "signal-anticlockwise-circle-arrow",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1556086784
                  },
                  {
                    "index": 368,
                    "type": "virtual",
                    "name": "signal-input",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1560281088
                  },
                  {
                    "index": 369,
                    "type": "virtual",
                    "name": "signal-output",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1564475392
                  },
                  {
                    "index": 370,
                    "type": "virtual",
                    "name": "signal-fuel",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1568669696
                  },
                  {
                    "index": 371,
                    "type": "virtual",
                    "name": "signal-lightning",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1572864000
                  },
                  {
                    "index": 372,
                    "type": "virtual",
                    "name": "signal-battery-low",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1577058304
                  },
                  {
                    "index": 373,
                    "type": "virtual",
                    "name": "signal-battery-mid-level",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1581252608
                  },
                  {
                    "index": 374,
                    "type": "virtual",
                    "name": "signal-battery-full",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1585446912
                  },
                  {
                    "index": 375,
                    "type": "virtual",
                    "name": "signal-radioactivity",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1589641216
                  },
                  {
                    "index": 376,
                    "type": "virtual",
                    "name": "signal-thermometer-blue",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1593835520
                  },
                  {
                    "index": 377,
                    "type": "virtual",
                    "name": "signal-thermometer-red",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1598029824
                  },
                  {
                    "index": 378,
                    "type": "virtual",
                    "name": "signal-fire",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1602224128
                  },
                  {
                    "index": 379,
                    "type": "virtual",
                    "name": "signal-snowflake",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1606418432
                  },
                  {
                    "index": 380,
                    "type": "virtual",
                    "name": "signal-explosion",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1610612736
                  },
                  {
                    "index": 381,
                    "type": "virtual",
                    "name": "signal-liquid",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1614807040
                  },
                  {
                    "index": 382,
                    "type": "virtual",
                    "name": "signal-stack-size",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1619001344
                  },
                  {
                    "index": 383,
                    "type": "virtual",
                    "name": "signal-recycle",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1623195648
                  },
                  {
                    "index": 384,
                    "type": "virtual",
                    "name": "signal-trash-bin",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1627389952
                  },
                  {
                    "index": 385,
                    "type": "virtual",
                    "name": "signal-science-pack",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1631584256
                  },
                  {
                    "index": 386,
                    "type": "virtual",
                    "name": "signal-map-marker",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1635778560
                  },
                  {
                    "index": 387,
                    "type": "virtual",
                    "name": "signal-white-flag",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1639972864
                  },
                  {
                    "index": 388,
                    "type": "virtual",
                    "name": "signal-lock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1644167168
                  },
                  {
                    "index": 389,
                    "type": "virtual",
                    "name": "signal-unlock",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1648361472
                  },
                  {
                    "index": 390,
                    "type": "virtual",
                    "name": "signal-speed",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1652555776
                  },
                  {
                    "index": 391,
                    "type": "virtual",
                    "name": "signal-ghost",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1656750080
                  },
                  {
                    "index": 392,
                    "type": "virtual",
                    "name": "signal-hourglass",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1660944384
                  },
                  {
                    "index": 393,
                    "type": "virtual",
                    "name": "signal-alarm",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1665138688
                  },
                  {
                    "index": 394,
                    "type": "virtual",
                    "name": "signal-sun",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1669332992
                  },
                  {
                    "index": 395,
                    "type": "virtual",
                    "name": "signal-moon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1673527296
                  },
                  {
                    "index": 396,
                    "type": "virtual",
                    "name": "signal-mining",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1677721600
                  },
                  {
                    "index": 397,
                    "type": "virtual",
                    "name": "signal-skull",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1681915904
                  },
                  {
                    "index": 398,
                    "type": "virtual",
                    "name": "signal-damage",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1686110208
                  },
                  {
                    "index": 399,
                    "type": "virtual",
                    "name": "signal-weapon",
                    "quality": "normal",
                    "comparator": "=",
                    "count": 1690304512
                  }
                ]
              }
            ]
          }
        }
      }
    ],
    "item": "blueprint",
    "version": 562949957025792
  }
}
"""