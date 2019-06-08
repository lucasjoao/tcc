#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
    visualize_features(data)
    visualize_labels(data)


def visualize_features(data):
    print('fazer gráfico agrupados para todas as vars escolhidas')


def visualize_labels(data):
    label_01 = 'Do you currently have a mental health disorder?'
    label_02 = 'Have you had a mental health disorder in the past?'
    label_03 = 'Have you ever sought treatment for a mental health ' + \
               'disorder from a mental health professional?'

    # answers to label 01 and label 02
    # label 03 use 1 and 0
    answer_yes = 'Yes'
    answer_no = 'No'
    answer_possibly = 'Possibly'
    answer_dont_know = 'Don\'t Know'

    label_data = data[[label_01, label_02, label_03]].copy()

    counted_01 = label_data[label_01].value_counts()
    counted_02 = label_data[label_02].value_counts()
    counted_03 = label_data[label_03].value_counts()

    # tuples with values that will fill the chart
    yes_values = (counted_01[answer_yes],
                  counted_02[answer_yes],
                  counted_03[1])
    no_values = (counted_01[answer_no],
                 counted_02[answer_no],
                 counted_03[0])
    # i know after execute some times that the third label don't has value
    possibly_values = (counted_01[answer_possibly],
                       counted_02[answer_possibly],
                       0)
    # i know after execute some times that the third label don't has value
    dk_values = (counted_01[answer_dont_know],
                 counted_02[answer_dont_know],
                 0)

    # to define the bar's positions
    ind = np.arange(len(yes_values))
    width = 0.2

    # first argument says the bar's positions
    # color = green
    plt.bar(ind, yes_values, width, label=answer_yes, color=(0.4, 0.5, 0.3, 1))
    # color = red
    plt.bar(ind + width, no_values, width, label=answer_no, color=(0.9, 0.2, 0.2, 1))
    # color = blue
    plt.bar(ind + 2 * width, possibly_values, width, label=answer_possibly,
            color=(0.4, 0.3, 0.8, 1))
    # color = yellow
    plt.bar(ind + 3 * width, dk_values, width, label=answer_dont_know,
            color=(0.9, 0.8, 0, 1))

    # the text will say what is Q1, Q2 and Q3
    plt.xticks(ind + 1.5 * width, ('Q1', 'Q2', 'Q3'))

    plt.title('Valores que serão utilizados como label')
    plt.xlabel('Perguntas')
    plt.ylabel('Número de respostas')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

if __name__ == '__main__':
    # path changes if you run this inside src directory
    path = 'datasets/OSMI_Mental_Health_in_Tech_Survey_2018.csv'
    data_original = pd.read_csv(path)
    print('Original data shape:', data_original.shape)

    data_filtered = initial_filter(data_original)
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
