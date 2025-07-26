from django.db import models

class Cliente(models.Model):
    codice = models.AutoField(primary_key=True)
    codice_fiscale = models.CharField(max_length=16)
    ragione_sociale = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=200)
    citta = models.CharField(max_length=100)

    def __str__(self):
        return self.ragione_sociale

class Utenza(models.Model):
    STATI = (
        ('attivo', 'Attivo'),
        ('inattivo', 'Inattivo'),
    )
    
    codice = models.AutoField(primary_key=True)
    data_apertura = models.DateField()
    indirizzo = models.CharField(max_length=200)
    citta = models.CharField(max_length=100)
    data_chiusura = models.DateField(null=True, blank=True)
    stato = models.CharField(max_length=10, choices=STATI)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Utenza {self.codice} - {self.indirizzo}"

class Fattura(models.Model):
    codice = models.AutoField(primary_key=True)
    data = models.DateField()
    imponibile = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    totale = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Fattura {self.codice}"

class Lettura(models.Model):
    codice = models.AutoField(primary_key=True)
    utenza = models.ForeignKey(Utenza, on_delete=models.CASCADE)
    fattura = models.ForeignKey(Fattura, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField()
    valore = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Lettura {self.codice} ({self.utenza})"