# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Integer, MetaData, Numeric, String, Table, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

metadata = MetaData()


t_attribute_definition = Table(
    'attribute_definition', metadata,
    Column('attribute_definition_id', Integer, nullable=False),
    Column('attribute_name', String(255), nullable=False),
    Column('attribute_description', Text),
    Column('attribute_type_concept_id', Integer, nullable=False),
    Column('attribute_syntax', Text)
)


t_care_site = Table(
    'care_site', metadata,
    Column('care_site_id', Integer, nullable=False),
    Column('care_site_name', String(255)),
    Column('place_of_service_concept_id', Integer),
    Column('location_id', Integer),
    Column('care_site_source_value', String(50)),
    Column('place_of_service_source_value', String(50))
)


t_cdm_source = Table(
    'cdm_source', metadata,
    Column('cdm_source_name', String(255), nullable=False),
    Column('cdm_source_abbreviation', String(25)),
    Column('cdm_holder', String(255)),
    Column('source_description', Text),
    Column('source_documentation_reference', String(255)),
    Column('cdm_etl_reference', String(255)),
    Column('source_release_date', Date),
    Column('cdm_release_date', Date),
    Column('cdm_version', String(10)),
    Column('vocabulary_version', String(20))
)


# t_cohort = Table(
#     'cohort', metadata,
#     Column('cohort_definition_id', Integer, nullable=False),
#     Column('subject_id', Integer, nullable=False),
#     Column('cohort_start_date', Date, nullable=False),
#     Column('cohort_end_date', Date, nullable=False)
# )

class Cohort(Base):
    __tablename__ = 'cohort'
    cohort_definition_id = Column(Integer, ForeignKey('cohort_definition.cohort_definition_id'), primary_key=True)
    subject_id = Column(Integer, primary_key=True)
    cohort_start_date = Column(Date, nullable=False)
    cohort_end_date = Column(Date, nullable=False)

    person = relationship("Person", backref=backref("cohort", uselist=False))
    
    def __str__(self):
        return f"<TableName(cohort_definition_id={self.cohort_definition_id}, subject_id={self.subject_id})>"


t_cohort_attribute = Table(
    'cohort_attribute', metadata,
    Column('cohort_definition_id', Integer, nullable=False),
    Column('cohort_start_date', Date, nullable=False),
    Column('cohort_end_date', Date, nullable=False),
    Column('subject_id', Integer, nullable=False),
    Column('attribute_definition_id', Integer, nullable=False),
    Column('value_as_number', Numeric),
    Column('value_as_concept_id', Integer)
)


t_cohort_definition = Table(
    'cohort_definition', metadata,
    Column('cohort_definition_id', Integer, nullable=False),
    Column('cohort_definition_name', String(255), nullable=False),
    Column('cohort_definition_description', Text),
    Column('definition_type_concept_id', Integer, nullable=False),
    Column('cohort_definition_syntax', Text),
    Column('subject_concept_id', Integer, nullable=False),
    Column('cohort_initiation_date', Date)
)

class CohortDefinition(Base):
    __tablename__ = 'cohort_definition'
    cohort_definition_id = Column(Integer, primary_key=True)
    cohort_definition_name = Column(String(255), primary_key=True)
    cohort_definition_description = Column(Text)
    definition_type_concept_id = Column(Integer, nullable=False)
    cohort_definition_syntax = Column(Text)
    subject_concept_id = Column(Integer, nullable=False)
    cohort_initiation_date = Column(Date, nullable=False)

    cohorts = relationship("Cohort", backref="definition")
    
    def __str__(self):
        return f"<{self.__tablename__}(cohort_definition_id={self.cohort_definition_id}, cohort_definition_name={self.cohort_definition_name})>"


t_concept = Table(
    'concept', metadata,
    Column('concept_id', Integer, nullable=False),
    Column('concept_name', String(255), nullable=False),
    Column('domain_id', String(20), nullable=False),
    Column('vocabulary_id', String(20), nullable=False),
    Column('concept_class_id', String(20), nullable=False),
    Column('standard_concept', String(1)),
    Column('concept_code', String(50), nullable=False),
    Column('valid_start_date', Date, nullable=False),
    Column('valid_end_date', Date, nullable=False),
    Column('invalid_reason', String(1))
)


t_concept_ancestor = Table(
    'concept_ancestor', metadata,
    Column('ancestor_concept_id', Integer, nullable=False),
    Column('descendant_concept_id', Integer, nullable=False),
    Column('min_levels_of_separation', Integer, nullable=False),
    Column('max_levels_of_separation', Integer, nullable=False)
)


t_concept_class = Table(
    'concept_class', metadata,
    Column('concept_class_id', String(20), nullable=False),
    Column('concept_class_name', String(255), nullable=False),
    Column('concept_class_concept_id', Integer, nullable=False)
)

class ConceptClass(Base):
    __tablename__ = 'concept_class'
    concept_class_id = Column(String(20), primary_key=True)
    concept_class_name = Column(String(255),nullable=False)
    concept_class_concept_id = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<TableName(concept_class_name={self.concept_class_name})>"
    
    def __repr__(self):
        return "<TableName(concept_class_id='%s')>" % self.concept_class_id


t_concept_relationship = Table(
    'concept_relationship', metadata,
    Column('concept_id_1', Integer, nullable=False),
    Column('concept_id_2', Integer, nullable=False),
    Column('relationship_id', String(20), nullable=False),
    Column('valid_start_date', Date, nullable=False),
    Column('valid_end_date', Date, nullable=False),
    Column('invalid_reason', String(1))
)


t_concept_synonym = Table(
    'concept_synonym', metadata,
    Column('concept_id', Integer, nullable=False),
    Column('concept_synonym_name', String(1000), nullable=False),
    Column('language_concept_id', Integer, nullable=False)
)


t_condition_era = Table(
    'condition_era', metadata,
    Column('condition_era_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('condition_concept_id', Integer, nullable=False),
    Column('condition_era_start_date', Date, nullable=False),
    Column('condition_era_end_date', Date, nullable=False),
    Column('condition_occurrence_count', Integer)
)


t_condition_occurrence = Table(
    'condition_occurrence', metadata,
    Column('condition_occurrence_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('condition_concept_id', Integer, nullable=False),
    Column('condition_start_date', Date, nullable=False),
    Column('condition_start_datetime', DateTime, nullable=False),
    Column('condition_end_date', Date),
    Column('condition_end_datetime', DateTime),
    Column('condition_type_concept_id', Integer, nullable=False),
    Column('stop_reason', String(20)),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('condition_source_value', String(50)),
    Column('condition_source_concept_id', Integer),
    Column('condition_status_source_value', String(50)),
    Column('condition_status_concept_id', Integer)
)


t_cost = Table(
    'cost', metadata,
    Column('cost_id', Integer, nullable=False),
    Column('cost_event_id', Integer, nullable=False),
    Column('cost_domain_id', String(20), nullable=False),
    Column('cost_type_concept_id', Integer, nullable=False),
    Column('currency_concept_id', Integer),
    Column('total_charge', Numeric),
    Column('total_cost', Numeric),
    Column('total_paid', Numeric),
    Column('paid_by_payer', Numeric),
    Column('paid_by_patient', Numeric),
    Column('paid_patient_copay', Numeric),
    Column('paid_patient_coinsurance', Numeric),
    Column('paid_patient_deductible', Numeric),
    Column('paid_by_primary', Numeric),
    Column('paid_ingredient_cost', Numeric),
    Column('paid_dispensing_fee', Numeric),
    Column('payer_plan_period_id', Integer),
    Column('amount_allowed', Numeric),
    Column('revenue_code_concept_id', Integer),
    Column('reveue_code_source_value', String(50)),
    Column('drg_concept_id', Integer),
    Column('drg_source_value', String(3))
)


t_death = Table(
    'death', metadata,
    Column('person_id', Integer, nullable=False),
    Column('death_date', Date, nullable=False),
    Column('death_datetime', DateTime),
    Column('death_type_concept_id', Integer, nullable=False),
    Column('cause_concept_id', Integer),
    Column('cause_source_value', String(50)),
    Column('cause_source_concept_id', Integer)
)


t_device_exposure = Table(
    'device_exposure', metadata,
    Column('device_exposure_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('device_concept_id', Integer, nullable=False),
    Column('device_exposure_start_date', Date, nullable=False),
    Column('device_exposure_start_datetime', DateTime, nullable=False),
    Column('device_exposure_end_date', Date),
    Column('device_exposure_end_datetime', DateTime),
    Column('device_type_concept_id', Integer, nullable=False),
    Column('unique_device_id', String(50)),
    Column('quantity', Integer),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('device_source_value', String(100)),
    Column('device_source_concept_id', Integer)
)


t_domain = Table(
    'domain', metadata,
    Column('domain_id', String(20), nullable=False),
    Column('domain_name', String(255), nullable=False),
    Column('domain_concept_id', Integer, nullable=False)
)


t_dose_era = Table(
    'dose_era', metadata,
    Column('dose_era_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('drug_concept_id', Integer, nullable=False),
    Column('unit_concept_id', Integer, nullable=False),
    Column('dose_value', Numeric, nullable=False),
    Column('dose_era_start_date', Date, nullable=False),
    Column('dose_era_end_date', Date, nullable=False)
)


t_drug_era = Table(
    'drug_era', metadata,
    Column('drug_era_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('drug_concept_id', Integer, nullable=False),
    Column('drug_era_start_date', Date, nullable=False),
    Column('drug_era_end_date', Date, nullable=False),
    Column('drug_exposure_count', Integer),
    Column('gap_days', Integer)
)


t_drug_exposure = Table(
    'drug_exposure', metadata,
    Column('drug_exposure_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('drug_concept_id', Integer, nullable=False),
    Column('drug_exposure_start_date', Date, nullable=False),
    Column('drug_exposure_start_datetime', DateTime, nullable=False),
    Column('drug_exposure_end_date', Date, nullable=False),
    Column('drug_exposure_end_datetime', DateTime),
    Column('verbatim_end_date', Date),
    Column('drug_type_concept_id', Integer, nullable=False),
    Column('stop_reason', String(20)),
    Column('refills', Integer),
    Column('quantity', Numeric),
    Column('days_supply', Integer),
    Column('sig', Text),
    Column('route_concept_id', Integer),
    Column('lot_number', String(50)),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('drug_source_value', String(50)),
    Column('drug_source_concept_id', Integer),
    Column('route_source_value', String(50)),
    Column('dose_unit_source_value', String(50))
)


t_drug_strength = Table(
    'drug_strength', metadata,
    Column('drug_concept_id', Integer, nullable=False),
    Column('ingredient_concept_id', Integer, nullable=False),
    Column('amount_value', Numeric),
    Column('amount_unit_concept_id', Integer),
    Column('numerator_value', Numeric),
    Column('numerator_unit_concept_id', Integer),
    Column('denominator_value', Numeric),
    Column('denominator_unit_concept_id', Integer),
    Column('box_size', Integer),
    Column('valid_start_date', Date, nullable=False),
    Column('valid_end_date', Date, nullable=False),
    Column('invalid_reason', String(1))
)


t_fact_relationship = Table(
    'fact_relationship', metadata,
    Column('domain_concept_id_1', Integer, nullable=False),
    Column('fact_id_1', Integer, nullable=False),
    Column('domain_concept_id_2', Integer, nullable=False),
    Column('fact_id_2', Integer, nullable=False),
    Column('relationship_concept_id', Integer, nullable=False)
)


t_location = Table(
    'location', metadata,
    Column('location_id', Integer, nullable=False),
    Column('address_1', String(50)),
    Column('address_2', String(50)),
    Column('city', String(50)),
    Column('state', String(2)),
    Column('zip', String(9)),
    Column('county', String(20)),
    Column('location_source_value', String(50))
)


t_measurement = Table(
    'measurement', metadata,
    Column('measurement_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('measurement_concept_id', Integer, nullable=False),
    Column('measurement_date', Date, nullable=False),
    Column('measurement_datetime', DateTime),
    Column('measurement_type_concept_id', Integer, nullable=False),
    Column('operator_concept_id', Integer),
    Column('value_as_number', Numeric),
    Column('value_as_concept_id', Integer),
    Column('unit_concept_id', Integer),
    Column('range_low', Numeric),
    Column('range_high', Numeric),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('measurement_source_value', String(50)),
    Column('measurement_source_concept_id', Integer),
    Column('unit_source_value', String(50)),
    Column('value_source_value', String(50))
)


t_note = Table(
    'note', metadata,
    Column('note_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('note_date', Date, nullable=False),
    Column('note_datetime', DateTime),
    Column('note_type_concept_id', Integer, nullable=False),
    Column('note_class_concept_id', Integer, nullable=False),
    Column('note_title', String(250)),
    Column('note_text', Text, nullable=False),
    Column('encoding_concept_id', Integer, nullable=False),
    Column('language_concept_id', Integer, nullable=False),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('note_source_value', String(50))
)


t_note_nlp = Table(
    'note_nlp', metadata,
    Column('note_nlp_id', BigInteger, nullable=False),
    Column('note_id', Integer, nullable=False),
    Column('section_concept_id', Integer),
    Column('snippet', String(250)),
    Column('offset', String(250)),
    Column('lexical_variant', String(250), nullable=False),
    Column('note_nlp_concept_id', Integer),
    Column('note_nlp_source_concept_id', Integer),
    Column('nlp_system', String(250)),
    Column('nlp_date', Date, nullable=False),
    Column('nlp_datetime', DateTime),
    Column('term_exists', String(1)),
    Column('term_temporal', String(50)),
    Column('term_modifiers', String(2000))
)


t_observation = Table(
    'observation', metadata,
    Column('observation_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('observation_concept_id', Integer, nullable=False),
    Column('observation_date', Date, nullable=False),
    Column('observation_datetime', DateTime),
    Column('observation_type_concept_id', Integer, nullable=False),
    Column('value_as_number', Numeric),
    Column('value_as_string', String(60)),
    Column('value_as_concept_id', Integer),
    Column('qualifier_concept_id', Integer),
    Column('unit_concept_id', Integer),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('observation_source_value', String(50)),
    Column('observation_source_concept_id', Integer),
    Column('unit_source_value', String(50)),
    Column('qualifier_source_value', String(50))
)


t_observation_period = Table(
    'observation_period', metadata,
    Column('observation_period_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('observation_period_start_date', Date, nullable=False),
    Column('observation_period_end_date', Date, nullable=False),
    Column('period_type_concept_id', Integer, nullable=False)
)


t_payer_plan_period = Table(
    'payer_plan_period', metadata,
    Column('payer_plan_period_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('payer_plan_period_start_date', Date, nullable=False),
    Column('payer_plan_period_end_date', Date, nullable=False),
    Column('payer_source_value', String(50)),
    Column('plan_source_value', String(50)),
    Column('family_source_value', String(50))
)


t_person = Table(
    'person', metadata,
    Column('person_id', Integer, nullable=False),
    Column('gender_concept_id', Integer, nullable=False),
    Column('year_of_birth', Integer, nullable=False),
    Column('month_of_birth', Integer),
    Column('day_of_birth', Integer),
    Column('birth_datetime', DateTime),
    Column('race_concept_id', Integer, nullable=False),
    Column('ethnicity_concept_id', Integer, nullable=False),
    Column('location_id', Integer),
    Column('provider_id', Integer),
    Column('care_site_id', Integer),
    Column('person_source_value', String(50)),
    Column('gender_source_value', String(50)),
    Column('gender_source_concept_id', Integer),
    Column('race_source_value', String(50)),
    Column('race_source_concept_id', Integer),
    Column('ethnicity_source_value', String(50)),
    Column('ethnicity_source_concept_id', Integer)
)

# TODO
class Person(Base):
    __tablename__ = 'person'
    cohort_definition_id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, primary_key=True)
    cohort_start_date = Column(Date, nullable=False)
    cohort_end_date = Column(Date, nullable=False)
    
    def __str__(self):
        return f"<TableName(cohort_definition_id={self.cohort_definition_id}, subject_id={self.subject_id})>"


t_procedure_occurrence = Table(
    'procedure_occurrence', metadata,
    Column('procedure_occurrence_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('procedure_concept_id', Integer, nullable=False),
    Column('procedure_date', Date, nullable=False),
    Column('procedure_datetime', DateTime, nullable=False),
    Column('procedure_type_concept_id', Integer, nullable=False),
    Column('modifier_concept_id', Integer),
    Column('quantity', Integer),
    Column('provider_id', Integer),
    Column('visit_occurrence_id', Integer),
    Column('procedure_source_value', String(50)),
    Column('procedure_source_concept_id', Integer),
    Column('qualifier_source_value', String(50))
)


t_provider = Table(
    'provider', metadata,
    Column('provider_id', Integer, nullable=False),
    Column('provider_name', String(255)),
    Column('npi', String(20)),
    Column('dea', String(20)),
    Column('specialty_concept_id', Integer),
    Column('care_site_id', Integer),
    Column('year_of_birth', Integer),
    Column('gender_concept_id', Integer),
    Column('provider_source_value', String(50)),
    Column('specialty_source_value', String(50)),
    Column('specialty_source_concept_id', Integer),
    Column('gender_source_value', String(50)),
    Column('gender_source_concept_id', Integer)
)


t_relationship = Table(
    'relationship', metadata,
    Column('relationship_id', String(20), nullable=False),
    Column('relationship_name', String(255), nullable=False),
    Column('is_hierarchical', String(1), nullable=False),
    Column('defines_ancestry', String(1), nullable=False),
    Column('reverse_relationship_id', String(20), nullable=False),
    Column('relationship_concept_id', Integer, nullable=False)
)


t_source_to_concept_map = Table(
    'source_to_concept_map', metadata,
    Column('source_code', String(50), nullable=False),
    Column('source_concept_id', Integer, nullable=False),
    Column('source_vocabulary_id', String(20), nullable=False),
    Column('source_code_description', String(255)),
    Column('target_concept_id', Integer, nullable=False),
    Column('target_vocabulary_id', String(20), nullable=False),
    Column('valid_start_date', Date, nullable=False),
    Column('valid_end_date', Date, nullable=False),
    Column('invalid_reason', String(1))
)


t_specimen = Table(
    'specimen', metadata,
    Column('specimen_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('specimen_concept_id', Integer, nullable=False),
    Column('specimen_type_concept_id', Integer, nullable=False),
    Column('specimen_date', Date, nullable=False),
    Column('specimen_datetime', DateTime),
    Column('quantity', Numeric),
    Column('unit_concept_id', Integer),
    Column('anatomic_site_concept_id', Integer),
    Column('disease_status_concept_id', Integer),
    Column('specimen_source_id', String(50)),
    Column('specimen_source_value', String(50)),
    Column('unit_source_value', String(50)),
    Column('anatomic_site_source_value', String(50)),
    Column('disease_status_source_value', String(50))
)


t_visit_occurrence = Table(
    'visit_occurrence', metadata,
    Column('visit_occurrence_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('visit_concept_id', Integer, nullable=False),
    Column('visit_start_date', Date, nullable=False),
    Column('visit_start_datetime', DateTime),
    Column('visit_end_date', Date, nullable=False),
    Column('visit_end_datetime', DateTime),
    Column('visit_type_concept_id', Integer, nullable=False),
    Column('provider_id', Integer),
    Column('care_site_id', Integer),
    Column('visit_source_value', String(50)),
    Column('visit_source_concept_id', Integer),
    Column('admitting_source_concept_id', Integer),
    Column('admitting_source_value', String(50)),
    Column('discharge_to_concept_id', Integer),
    Column('discharge_to_source_value', String(50)),
    Column('preceding_visit_occurrence_id', Integer)
)


t_vocabulary = Table(
    'vocabulary', metadata,
    Column('vocabulary_id', String(20), nullable=False),
    Column('vocabulary_name', String(255), nullable=False),
    Column('vocabulary_reference', String(255)),
    Column('vocabulary_version', String(255)),
    Column('vocabulary_concept_id', Integer, nullable=False)
)
