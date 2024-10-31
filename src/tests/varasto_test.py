import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_negatiivinen(self):
        negatiivinen_vararasto=Varasto(-10)
        self.assertAlmostEqual(negatiivinen_vararasto.tilavuus,0)

    def test_alku_saldo_negatiivinen(self):
        negatiivinen_vararasto=Varasto(2,-10)
        self.assertAlmostEqual(negatiivinen_vararasto.saldo,0)

    def test_alku_saldo_suurempi(self):
        negatiivinen_vararasto=Varasto(1,10)
        self.assertAlmostEqual(negatiivinen_vararasto.saldo,1)

    def test_lisaa_varastoon_negatiivinen(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo,0)
    
    def test_liikaa_varastoon(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_ota_varastosta_negativiinen(self):
        otetut=self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(otetut,0)

    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        kaikki=self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(kaikki,10)
    def test_string_print(self):
        oletus_tuloste=f"saldo = 0, vielä tilaa 10"
        self.assertEqual(oletus_tuloste,str(self.varasto))
