from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


# ============================================================
# Destination Information Tool
# ============================================================

class DestinationInfoInput(BaseModel):
    destination: str = Field(
        ...,
        description="Name of the travel destination."
    )


class DestinationInfoTool(BaseTool):
    name: str = "DestinationInfoTool"

    description: str = (
        "Provides basic travel information about a destination, "
        "including major attractions, best time to visit, "
        "and general travel information."
    )

    args_schema: Type[BaseModel] = DestinationInfoInput

    # Used only for the deliberate failure experiment.
    _failed_once: bool = False

    def _run(self, destination: str) -> str:

        # ----------------------------------------------------
        # DELIBERATE TOOL FAILURE
        # ----------------------------------------------------

        if not self._failed_once:
            self._failed_once = True

            raise RuntimeError(
                "DELIBERATE TEST FAILURE: "
                "Destination information service temporarily unavailable."
            )

        # ----------------------------------------------------
        # Normal successful execution
        # ----------------------------------------------------

        destination_data = {
            "Delhi": {
                "attractions": [
                    "Red Fort",
                    "India Gate",
                    "Qutub Minar",
                    "Humayun's Tomb",
                ],
                "best_time": "October to March",
                "travel_info": (
                    "Major Indian city with extensive road, "
                    "rail, and air connectivity."
                ),
            },

            "Goa": {
                "attractions": [
                    "Baga Beach",
                    "Fort Aguada",
                    "Basilica of Bom Jesus",
                    "Dudhsagar Falls",
                ],
                "best_time": "November to February",
                "travel_info": (
                    "Popular coastal destination known for "
                    "beaches, nightlife, and Portuguese heritage."
                ),
            },

            "Dubai": {
                "attractions": [
                    "Burj Khalifa",
                    "Dubai Mall",
                    "Palm Jumeirah",
                    "Dubai Marina",
                ],
                "best_time": "November to March",
                "travel_info": (
                    "International tourism hub with extensive "
                    "air connectivity and modern infrastructure."
                ),
            },
        }

        data = destination_data.get(
            destination.title()
        )

        if data is None:
            return (
                f"Destination: {destination}\n"
                "Major attractions: local landmarks, museums, "
                "markets, cultural sites, and outdoor activities.\n"
                "Best time: Depends on local climate and season.\n"
                "Travel information: Research local transport, "
                "visa requirements, accommodation, and weather "
                "before travelling."
            )

        return (
            f"Destination: {destination}\n"
            f"Major attractions: {', '.join(data['attractions'])}\n"
            f"Best time to visit: {data['best_time']}\n"
            f"Travel information: {data['travel_info']}"
        )


# ============================================================
# Cost Calculator Tool
# ============================================================

class CostCalculatorInput(BaseModel):
    destination: str = Field(
        ...,
        description="Travel destination."
    )

    days: int = Field(
        ...,
        description="Number of travel days.",
        ge=1,
        le=30,
    )

    travelers: int = Field(
        ...,
        description="Number of travelers.",
        ge=1,
        le=10,
    )


class CostCalculatorTool(BaseTool):
    name: str = "CostCalculatorTool"

    description: str = (
        "Calculates an estimated travel budget including "
        "accommodation, food, transportation, and activities."
    )

    args_schema: Type[BaseModel] = CostCalculatorInput

    def _run(
        self,
        destination: str,
        days: int,
        travelers: int,
    ) -> str:

        # Simple illustrative estimates.
        # Values are intentionally approximate.

        daily_costs = {
            "Delhi": {
                "accommodation": 3000,
                "food": 1200,
                "transportation": 600,
                "activities": 800,
            },

            "Goa": {
                "accommodation": 3500,
                "food": 1500,
                "transportation": 800,
                "activities": 1200,
            },

            "Dubai": {
                "accommodation": 7000,
                "food": 2500,
                "transportation": 1500,
                "activities": 3000,
            },
        }

        costs = daily_costs.get(
            destination.title(),
            {
                "accommodation": 4000,
                "food": 1500,
                "transportation": 1000,
                "activities": 1200,
            },
        )

        accommodation = (
            costs["accommodation"]
            * days
            * travelers
        )

        food = (
            costs["food"]
            * days
            * travelers
        )

        transportation = (
            costs["transportation"]
            * days
            * travelers
        )

        activities = (
            costs["activities"]
            * days
            * travelers
        )

        total = (
            accommodation
            + food
            + transportation
            + activities
        )

        return (
            f"Destination: {destination}\n"
            f"Travelers: {travelers}\n"
            f"Days: {days}\n\n"
            f"Estimated Accommodation: ₹{accommodation:,}\n"
            f"Estimated Food: ₹{food:,}\n"
            f"Estimated Transportation: ₹{transportation:,}\n"
            f"Estimated Activities: ₹{activities:,}\n"
            f"Estimated Total: ₹{total:,}"
        )