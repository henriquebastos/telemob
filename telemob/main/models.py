# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Campaign(models.Model):
    name = models.CharField('Nome da Campanha', max_length=150)
    description = models.TextField('Descrição da Campanha')
    date_created = models.DateField('Criado em', auto_now_add=True)
    last_updated = models.DateField('Última atualização em', auto_now=True)

    class Meta:
        verbose_name = 'Campanha'

    def __unicode__(self):
        return self.name


class Politician(models.Model):
    PARTY_CHOICES = (
        ('PMDB', 'PMDB - Partido Do Movimento Democrático Brasileiro'),
        ('PTB', 'PTB - Partido Trabalhista Brasileiro'),
        ('PDT', 'PDT - Partido Democrático Trabalhista'),
        ('PT', 'PT - Partido Dos Trabalhadores'),
        ('DEM', 'DEM - Democratas'),
        ('PCdoB', 'PCdoB - Partido Comunista Do Brasil'),
        ('PSB', 'PSB - Partido Socialista Brasileiro'),
        ('PSDB', 'PSDB - Partido Da Social Democracia Brasileira'),
        ('PTC', 'PTC - Partido Trabalhista Cristão'),
        ('PSC', 'PSC - Partido Social Cristão'),
        ('PMN', 'PMN - Partido Da Mobilização Nacional'),
        ('PRP', 'PRP - Partido Republicano Progressista'),
        ('PPS', 'PPS - Partido Popular Socialista'),
        ('PV',  'PV - Partido Verde'),
        ('PTdoB','PTdoB - Partido Trabalhista Do Brasil'),
        ('PP',  'PP - Partido Progressista'),
        ('PSTU', 'PSTU - Partido Socialista Dos Trabalhadores Unificado'),
        ('PCB', 'PCB - Partido Comunista Brasileiro'),
        ('PRTB', 'PRTB - Partido Renovador Trabalhista Brasileiro'),
        ('PHS', 'PHS - Partido Humanista Da Solidariedade'),
        ('PSDC', 'PSDC - Partido Social Democrata Cristão'),
        ('PCO', 'PCO - Partido Da Causa Operária'),
        ('PTN', 'PTN - Partido Trabalhista Nacional'),
        ('PSL', 'PSL - Partido Social Liberal'),
        ('PRB', 'PRB - Partido Republicano Brasileiro'),
        ('PSOL', 'PSOL - Partido Socialismo E Liberdade'),
        ('PR',  'PR - Partido Da República'),
        ('PSD', 'PSD - Partido Social Democrático'),
        ('PPL', 'PPL - Partido Pátria Livre'),
        ('PEN', 'PEN - Partido Ecológico Nacional'),
        ('PROS', 'PROS - Partido Republicano Da Ordem Social'),
        ('SDD ', 'SDD - Solidariedade'),
    )

    CATEGORY_CHOICES = (
        ('T', 'Titular'),
        ('S', 'Suplente'),
        ('E', 'Efetivo')
    )

    name = models.CharField('Nome', max_length=150)
    parliamentary_name = models.CharField('Nome Parlamentar', max_length=150)
    political_party = models.CharField('Partido', choices=PARTY_CHOICES, max_length=10)
    uf = models.CharField('UF', choices=STATE_CHOICES, max_length=10)
    category = models.CharField('Categoria', choices=CATEGORY_CHOICES, max_length=20)
    annex = models.IntegerField('Anexo', blank=True, null=True)
    chamber = models.IntegerField('Gabinete', blank=True, null=True)
    tel = models.CharField('Telefone', max_length=20)
    fax = models.CharField('Fax', max_length=20)
    email = models.EmailField('Email', max_length=100)
    date_created = models.DateField('Criado em', auto_now_add=True)
    last_updated = models.DateField('Última atualização em', auto_now=True)

    class Meta:
        verbose_name = 'Político'

    def __unicode__(self):
        return self.name


class Contact(models.Model):

    CONTACT_CHOICES = (
        ('tel', 'Telefone'),
        ('fax', 'Fax'),
        ('telegrama', 'Telegrama'),
        ('email', 'E-mail')
    )

    RESULT_CHOICES = (
        ('Telefonei', (
                ('0', 'Falei com o(a) Deputado(a) em pessoa'),
                ('1', 'Falei com outra pessoa'),
                ('2', 'Deixei recado em uma máquina'),
                ('3', 'Número ocupado'),
                ('4', 'Ninguém atendeu.'),
                ('5', 'Número inexistente ou outra falha')
            )
        ),
        ('Enviei telegrama', (
                ('6', 'Correio vai entregar no gabinete!'),
            )
        ),
        ('Enviei fax', (
                ('7', 'Transmissão bem sucedida'),
                ('8', 'Número ocupado'),
                ('9', 'Ninguém atendeu.'),
                ('10', 'Número inexistente ou outra falha')
            )
        ),
        ('Enviei e-mail', (
                ('11', 'Tomara que alguém leia!'),
            )
        ),
    )

    politician = models.ForeignKey(Politician, verbose_name='Político')
    campaign = models.ForeignKey(Campaign, verbose_name='Campanha')
    contacted_by = models.CharField(verbose_name='Contato via', choices=CONTACT_CHOICES, max_length=10, blank=True, null=True)
    result = models.CharField(verbose_name='Resultado do contato', choices=RESULT_CHOICES, max_length=10, blank=True, null=True)
    date_created = models.DateField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Contato'

    def __unicode__(self):
        return '%s - %s' % (self.campaign.name, self.politician.name)

class HelpText(models.Model):
    campaign = models.ForeignKey(Campaign, verbose_name='Texto de ajuda para a campanha')
    name = models.CharField('Nome da Ajuda', max_length=150)
    description = models.TextField('Texto de Ajuda')
    date_created = models.DateField('Criado em', auto_now_add=True)
    last_updated = models.DateField('Última atualização em', auto_now=True)

    class Meta:
        verbose_name = 'Texto de Ajuda'
        verbose_name_plural = 'Textos de Ajuda'

    def __unicode__(self):
        return self.name
