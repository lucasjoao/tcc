#!/usr/bin/env python
# coding: utf-8

import pandas as pd


def initial_filter(data):
    qst_01 = '<strong>Are you self-employed?</strong>'
    qst_02 = 'Is your primary role within your company related to tech/IT?'
    qst_03 = '<strong>Do you have previous employers?</strong>'

    is_self_employed = data[qst_01] == 1
    is_tech = data[qst_02] == 1.0
    has_previous_employers = data[qst_03] == 1

    filter_condition = (~is_self_employed | has_previous_employers) & is_tech
    return data[filter_condition]


def visualize_data(data):
    print('fazer gráfico agrupados para todas as vars escolhidas')
    print('fazer gráfico para resultados')
    label_01 = 'Do you currently have a mental health disorder?'
    label_02 = 'Have you had a mental health disorder in the past?'
    label_03 = 'Have you ever sought treatment for a mental health ' + \
               'disorder from a mental health professional?'

    label_data = data[[label_01, label_02, label_03]].copy()
    # TODO: printar label_data

if __name__ == '__main__':
    # path changes if you run this inside src directory
    data = pd.read_csv('datasets/OSMI_Mental_Health_in_Tech_Survey_2018.csv')
    print('Original data shape:', data.shape)

    data_filtered = initial_filter(data)
    print('Filtered data shape:', data_filtered.shape)

    visualize_data(data_filtered)

    print('ver notes por causa da limpeza')

# COLUNAS para usar - empresa
# Does your employer provide mental health benefits as part of healthcare coverage?
# Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?
# Does your employer offer resources to learn more about mental health disorders and options for seeking help?
# If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?
# Overall, how much importance does your employer place on mental health?
# Have your previous employers provided mental health benefits?
# Were you aware of the options for mental health care provided by your previous employers?
# Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?
# Did your previous employers provide resources to learn more about mental health disorders and how to seek help?
# Have you observed or experienced supportive or well handled responde to a mental health issue in your current or previous workplace?
# Have you observed or experienced an unsupportive or badly handled responde to a mental health issue in your current or previous workplace?
