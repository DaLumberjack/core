"""Data for creating nutrient classes."""

GENERAL_HYDROPONICS = (
    {
        "name": "General Hydroponics",
        "short_name": "gen_hydro",
        "models": {
            "liquid": {
                "unit": "mL/L",
                "flora": {
                    "micro": {
                        "npk": "0-5-4",
                        "derived_from": "Magnesium Carbonate, etc",
                        "suggested_feed": {
                            "growth_stage": {
                                "seedling": {
                                    "light": {
                                        "value": 0.48,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.53,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 0.66,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "early_growth": {
                                    "light": {
                                        "value": 0.95,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.11,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.38,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "mid_growth": {
                                    "light": {
                                        "value": 1.30,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.48,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.85,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "late_growth": {
                                    "light": {
                                        "value": 1.59,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.80,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 2.25,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "early_bloom": {
                                    "light": {
                                        "value": 1.40,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.61,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 2.01,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "mid_bloom": {
                                    "light": {
                                        "value": 1.22,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.4,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.75,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "late_bloom": {
                                    "light": {
                                        "value": 0.87,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.01,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.24,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "ripen": {
                                    "light": {
                                        "value": 0.53,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.61,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 0.74,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                            },
                        },
                    },
                    "gro": {
                        "npk": "0-5-4",
                        "derived_from": "Magnesium Carbonate, etc",
                        "suggested_feed": {
                            "growth_stage": {
                                "seedling": {
                                    "light": {
                                        "value": 0.48,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.53,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 0.66,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "early_growth": {
                                    "light": {
                                        "value": 0.9,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.01,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.27,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "mid_growth": {
                                    "light": {
                                        "value": 1.22,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.38,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.72,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "late_growth": {
                                    "light": {
                                        "value": 1.48,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.69,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 2.12,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "early_bloom": {
                                    "light": {
                                        "value": 1.22,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.40,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.75,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "mid_bloom": {
                                    "light": {
                                        "value": 1.22,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.4,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.75,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "late_bloom": {
                                    "light": {
                                        "value": 0.87,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.01,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.24,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "ripen": {
                                    "light": {
                                        "value": 0.53,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.61,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 0.74,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                            },
                        },
                    },
                    "bloom": {
                        "npk": "0-5-4",
                        "derived_from": "Magnesium Carbonate, etc",
                        "suggested_feed": {
                            "growth_stage": {
                                "seedling": {
                                    "light": {
                                        "value": 0.48,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.53,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 0.66,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "early_growth": {
                                    "light": {
                                        "value": 0.69,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.79,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 0.98,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "mid_growth": {
                                    "light": {
                                        "value": 0.9,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.01,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.27,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "late_growth": {
                                    "light": {
                                        "value": 1.11,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.27,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.59,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "early_bloom": {
                                    "light": {
                                        "value": 1.59,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.80,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 2.25,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "mid_bloom": {
                                    "light": {
                                        "value": 1.75,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 2.01,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 2.51,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "late_bloom": {
                                    "light": {
                                        "value": 1.06,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 1.22,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.51,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                                "ripen": {
                                    "light": {
                                        "value": 0.85,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "medium": {
                                        "value": 0.95,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                    "aggressive": {
                                        "value": 1.19,
                                        "min": 0.3,
                                        "max": 3,
                                        "step": 0.01,
                                    },
                                },
                            },
                        },
                    },
                },
                "ph": {
                    "up": {
                        "value": 0.05,
                        "min": 0.01,
                        "max": 0.3,
                        "step": 0.01,
                    },
                    "down": {
                        "value": 0.05,
                        "min": 0.01,
                        "max": 0.3,
                        "step": 0.01,
                    },
                },
            },
        },
    },
)
