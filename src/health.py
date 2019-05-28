#!/usr/bin/env python
# coding: utf-8

import pandas as pd

if __name__ == '__main__':
    # path changes if you run this inside src directory
    data = pd.read_csv('datasets/OSMI_Mental_Health_in_Tech_Survey_2018.csv')

    print('Original data shape:', data.shape)

    qst_01 = '<strong>Are you self-employed?</strong>'
    qst_02 = 'Is your primary role within your company related to tech/IT?'
    qst_03 = '<strong>Do you have previous employers?</strong>'

    is_self_employed = data[qst_01] == 1
    is_tech = data[qst_02] == 1.0
    has_previous_employers = data[qst_03] == 1

    filter_condition = (~is_self_employed | has_previous_employers) & is_tech
    data_filtered = data[filter_condition]

    print('Filtered data shape:', data_filtered.shape)

    # TODO: use next line way to get columns
    tmp_data = data_filtered[['#', qst_01]].copy()
    print(tmp_data.shape)
    print(tmp_data.head())

# TODO das técnicas
# usar regressão linear pada ds
# usar gráficos para dv

# COLUNAS para usar - empresa
# Does your employer provide mental health benefits as part of healthcare coverage?
# Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?
# Does your employer offer resources to learn more about mental health disorders and options for seeking help?
# (???) Do you know the options for mental health care available under your employer-provided health coverage? (???)
# (???) Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer? (???)
# If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?
# Overall, how much importance does your employer place on physical health?
# Overall, how much importance does your employer place on mental health?

# COLUNAS para usar - empresas passadas
# Have your previous employers provided mental health benefits?
# Were you aware of the options for mental health care provided by your previous employers?
# Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?
# Did your previous employers provide resources to learn more about mental health disorders and how to seek help?
# (???) Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers? (???)

# COLUNAS para usar - empresa atual e empresas passadas
# Have you observed or experienced supportive or well handled responde to a mental health issue in your current or previous workplace?
# Have you observed or experienced an unsupportive or badly handled responde to a mental health issue in your current or previous workplace?

# COLUNAS para usar - pessoa
# Would you feel more comfortable talking to your coworkers about your physical health or your mental health?
# Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?
# Have you ever discussed your mental health with your employer?
# Would you feel comfortable discussing a mental health issue with your coworkers?
# Have you ever discussed your mental health with coworkers?
# Have you ever had a coworker discuss their or another coworker's mental health with you?
# (???, não né) Do you have medical coverage (private insurance or state-provided) that includes treatment of mental health disorders? (???, não né)
# (???) Do you know local or online resources to seek help for a mental health issue? (???)
# If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to clients or business contacts?
# f you have been diagnosed or treated for a mental health disorder, do you ever reveal this to coworkers or employees?
# do you believe your productivity is ever affected by a mental health issue?
# Would you have felt more comfortable talking to your previous employer about your physical health or your mental health?
# Would you bring up your mental health with a potential employer in an interview?
# How willing would you be to share with friends and family that you have a mental illness?
# Did you ever discuss your mental health with a previous coworker(s)?
# Did you ever have a previous coworker discuss their or another coworker's mental health with you?

# COLUNAS para usar de resultado
# (???) Are you openly identified at work as a person with a mental health issue? (???)
# Do you currently have a mental health disorder?
# Have you had a mental health disorder in the past?
# Have you ever sought treatment for a mental health disorder from a mental health professional?
