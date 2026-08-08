"""
Report generation module - formats analysis into readable reports
"""

import json
from datetime import datetime

class ReportGenerator:
    """Generates formatted welfare reports from analysis data"""
    
    def generate_report(self, analysis: dict) -> str:
        """
        Generate a formatted report from analysis results
        
        Args:
            analysis: Dictionary containing analysis results
            
        Returns:
            Formatted report string
        """
        if analysis is None:
            return "❌ No analysis data available"
        
        report = []
        report.append(self._header())
        
        # Species and breed
        report.append(self._species_section(analysis))
        
        # Behavioral observations
        report.append(self._behavioral_section(analysis))
        
        # Physical observations
        report.append(self._physical_section(analysis))
        
        # Welfare assessment
        report.append(self._welfare_section(analysis))
        
        # Environment
        report.append(self._environment_section(analysis))
        
        # Medical observations
        report.append(self._medical_section(analysis))
        
        # Recommendations
        report.append(self._recommendations_section(analysis))
        
        # Disclaimers
        report.append(self._disclaimers_section(analysis))
        
        report.append(self._footer())
        
        return "\n".join(report)
    
    def _header(self) -> str:
        """Generate report header"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""╔═══════════════════════════════════════════════╗
║           🐾 GLOXPAW AI ANALYSIS 🐾          ║
║          Animal Welfare Assessment           ║
╚═══════════════════════════════════════════════╝

Generated: {timestamp}
"""
    
    def _species_section(self, analysis: dict) -> str:
        """Generate species identification section"""
        section = ["\n" + "="*50]
        section.append("SPECIES & BREED IDENTIFICATION")
        section.append("="*50)
        
        species = analysis.get("species", "Unknown")
        species_conf = analysis.get("species_confidence", 0)
        section.append(f"Species: {species}")
        if species_conf > 0:
            section.append(f"Confidence: {species_conf}%")
        
        breed = analysis.get("breed", "Unknown")
        breed_conf = analysis.get("breed_confidence", 0)
        breed_notes = analysis.get("breed_notes", "")
        
        if breed != "Unknown":
            section.append(f"\nLikely breed: {breed}")
            section.append(f"Confidence: {breed_conf}%")
            if breed_notes:
                section.append(f"Notes: {breed_notes}")
        
        return "\n".join(section)
    
    def _behavioral_section(self, analysis: dict) -> str:
        """Generate behavioral observations section"""
        section = ["\n" + "="*50]
        section.append("BEHAVIORAL OBSERVATIONS")
        section.append("="*50)
        
        behaviors = analysis.get("behavioral_observations", {})
        
        observation_keys = [
            ("posture", "Posture"),
            ("ear_position", "Ear Position"),
            ("tail_position", "Tail Position"),
            ("facial_expression", "Facial Expression"),
            ("overall_body_tension", "Body Tension"),
            ("eye_contact", "Eye Contact")
        ]
        
        for key, label in observation_keys:
            if key in behaviors and behaviors[key]:
                section.append(f"{label}: {behaviors[key]}")
        
        # Add behavioral interpretation
        interpretation = analysis.get("behavioral_interpretation", {})
        if interpretation:
            state = interpretation.get("primary_state", "Unknown")
            confidence = interpretation.get("confidence", 0)
            
            section.append(f"\nPrimary State: {state}")
            section.append(f"Confidence: {confidence}%")
            
            indicators = interpretation.get("indicators_supporting", [])
            if indicators:
                section.append("\nSupporting indicators:")
                for indicator in indicators:
                    section.append(f"  • {indicator}")
            
            caveats = interpretation.get("caveats", "")
            if caveats:
                section.append(f"\n⚠️  {caveats}")
        
        return "\n".join(section)
    
    def _physical_section(self, analysis: dict) -> str:
        """Generate physical observations section"""
        section = ["\n" + "="*50]
        section.append("PHYSICAL OBSERVATIONS")
        section.append("="*50)
        
        physical = analysis.get("physical_observations", {})
        
        if coat := physical.get("coat_condition"):
            section.append(f"Coat Condition: {coat}")
        
        if condition := physical.get("body_condition"):
            section.append(f"Body Condition: {condition}")
        
        if movement := physical.get("movement_ability"):
            section.append(f"Movement: {movement}")
        
        abnormalities = physical.get("visible_abnormalities", [])
        if abnormalities:
            section.append("\nVisible Observations:")
            for item in abnormalities:
                section.append(f"  • {item}")
        else:
            section.append("\nNo obvious visible abnormalities detected.")
        
        if features := physical.get("notable_features"):
            section.append(f"\nNotable Features: {features}")
        
        return "\n".join(section)
    
    def _medical_section(self, analysis: dict) -> str:
        """Generate medical observations section"""
        section = ["\n" + "="*50]
        section.append("⚠️  MEDICAL OBSERVATIONS (Visual Only)")
        section.append("="*50)
        section.append("\n🔴 IMPORTANT: This analysis cannot diagnose medical conditions.")
        section.append("A photo captures a single moment and cannot assess health.")
        
        medical = analysis.get("medical_observations", [])
        
        if medical:
            section.append("\nVisible observations that may warrant attention:")
            for observation in medical:
                section.append(f"  ⚠️  {observation}")
        else:
            section.append("\nNo obvious concerning visual indicators detected.")
        
        section.append("\n📋 For medical concerns, consult a veterinarian.")
        
        return "\n".join(section)
    
    def _welfare_section(self, analysis: dict) -> str:
        """Generate welfare assessment section"""
        section = ["\n" + "="*50]
        section.append("WELFARE ASSESSMENT")
        section.append("="*50)
        
        welfare = analysis.get("welfare_observations", {})
        
        # Handle if welfare_observations is a list instead of dict
        if isinstance(welfare, list):
            for item in welfare:
                section.append(f"\n• {item}")
            return "\n".join(section)
        
        # Handle dict structure
        if not isinstance(welfare, dict):
            welfare = {}
        
        # Positive indicators
        positive = welfare.get("positive_indicators", [])
        if positive:
            section.append("\n✅ Positive Indicators:")
            for indicator in positive:
                section.append(f"   ✓ {indicator}")
        
        # Concerns for observation
        concerns = welfare.get("concerns_for_observation", [])
        if concerns:
            section.append("\n⚠️  Observations Suggesting Possible Concern:")
            for concern in concerns:
                section.append(f"   • {concern}")
        
        # Cannot assess
        cannot = welfare.get("cannot_assess", [])
        if cannot:
            section.append("\n❌ Cannot Assess From Photo:")
            for item in cannot:
                section.append(f"   • {item}")
        
        return "\n".join(section)
    
    def _environment_section(self, analysis: dict) -> str:
        """Generate environment section"""
        section = ["\n" + "="*50]
        section.append("ENVIRONMENT")
        section.append("="*50)
        
        environment = analysis.get("environment", {})
        
        if setting := environment.get("setting"):
            section.append(f"Setting: {setting}")
        
        if conditions := environment.get("apparent_conditions"):
            section.append(f"Conditions: {conditions}")
        
        if enrichment := environment.get("enrichment"):
            section.append(f"Enrichment: {enrichment}")
        
        hazards = environment.get("hazards_visible", [])
        if isinstance(hazards, list):
            if hazards:
                section.append("\nPotential Hazards:")
                for hazard in hazards:
                    section.append(f"  ⚠️  {hazard}")
            else:
                section.append("\nNo obvious environmental hazards detected.")
        elif isinstance(hazards, str) and hazards:
            section.append(f"\nHazards: {hazards}")
        
        return "\n".join(section)
    
    def _recommendations_section(self, analysis: dict) -> str:
        """Generate recommendations section"""
        section = ["\n" + "="*50]
        section.append("RECOMMENDATIONS")
        section.append("="*50)
        
        recommendations = analysis.get("recommendations", {})
        
        if immediate := recommendations.get("immediate"):
            section.append(f"\n🔴 Immediate:\n{immediate}")
        
        if ongoing := recommendations.get("ongoing_observation"):
            section.append(f"\n📋 Ongoing Observation:\n{ongoing}")
        
        if care := recommendations.get("normal_care"):
            section.append(f"\n✅ Care Suggestions:\n{care}")
        
        if professional := recommendations.get("professional_consultation"):
            section.append(f"\n👨‍⚕️ Professional Consultation:\n{professional}")
        
        return "\n".join(section)
    
    def _disclaimers_section(self, analysis: dict) -> str:
        """Generate disclaimers section"""
        section = ["\n" + "="*50]
        section.append("⚠️  IMPORTANT DISCLAIMERS")
        section.append("="*50)
        
        section.append("""
📸 PHOTO LIMITATIONS:
   • A single photo is a snapshot in time
   • Behavior changes constantly with context
   • Environmental stress can change animal state rapidly
   • Historical behavior cannot be assessed from one image

🩺 MEDICAL LIMITATIONS:
   • This tool CANNOT diagnose medical conditions
   • Many health issues are NOT visible in photos
   • Pain, illness, and injuries may not show obvious signs
   • A veterinarian requires hands-on examination

🧠 BEHAVIORAL LIMITATIONS:
   • Mood interpretation is speculative even from observation
   • Individual animal personalities vary greatly
   • Species-typical behavior differs significantly
   • Anxiety, fear, and stress require context to interpret

✅ RECOMMENDED APPROACH:
   1. Use this analysis as ONE data point
   2. Observe the animal over TIME
   3. Note patterns, not single moments
   4. Consult professionals for medical/behavioral concerns
   5. Trust your knowledge of the individual animal

This tool supports animal welfare - it does not replace professional assessment.""")
        
        if analysis.get("analysis_limitations"):
            section.append(f"\n📝 Analysis Notes:\n{analysis['analysis_limitations']}")
        
        return "\n".join(section)
    
    def _footer(self) -> str:
        """Generate report footer"""
        return """
╔═══════════════════════════════════════════════╗
║  GloxPaw AI - Animal Welfare Assessment Tool  ║
║    For educational and observational use      ║
╚═══════════════════════════════════════════════╝
"""
