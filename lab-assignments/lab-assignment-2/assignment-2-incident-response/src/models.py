from pydantic import BaseModel, Field


class IncidentClassification(BaseModel):
    incident_type: str = Field(
        description="Category of the incident"
    )

    severity: str = Field(
        description="Low, Medium, High, or Critical"
    )

    affected_service: str

    probable_symptoms: list[str]

    initial_assessment: str


class InvestigationResult(BaseModel):
    affected_service: str

    logs: str

    metrics: str

    service_status: str

    investigation_summary: str

    information_quality: str


class IncidentResolutionReport(BaseModel):
    incident_id: str

    incident_type: str

    severity: str

    affected_service: str

    probable_cause: str

    evidence: list[str]

    recommended_actions: list[str]

    immediate_actions: list[str]

    long_term_prevention: list[str]

    resolution_confidence: float = Field(
        ge=0,
        le=100,
    )

    unresolved_information: list[str]