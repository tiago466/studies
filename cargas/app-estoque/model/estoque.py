

class Estoque:

    def __init__(self, cod_zt, cod_cli, desc_item, grupo, subgrupo, tipo_material, classificacao_item, classificacao_anvisa, ultima_entrada, ultima_saida, vl_item, saldo, dias_s_movto):
        self.cod_zt = cod_zt
        self.cod_cli = cod_cli
        self.desc_item = desc_item
        self.grupo = grupo
        self.subgrupo = subgrupo
        self.tipo_material = tipo_material
        self.classificacao_item = classificacao_item
        self.classificacao_anvisa = classificacao_anvisa
        self.ultima_entrada = ultima_entrada
        self.ultima_saida = ultima_saida
        self.vl_item = vl_item
        self.saldo = saldo
        self.dias_s_movto = dias_s_movto

    def get_cod_zt(self):
        return self.cod_zt
    
    def set_cod_zt(self, cod_zt):
        self.cod_zt = cod_zt

    def get_cod_cli(self):
        return self.cod_cli
    
    def set_cod_cli(self, cod_cli):
        self.cod_cli = cod_cli

    def get_desc_item(self):
        return self.desc_item
    
    def set_desc_item(self, desc_item):
        self.desc_item = desc_item

    def get_grupo(self):
        return self.grupo
    
    def set_grupo(self, grupo):
        self.grupo = grupo

    def get_subgrupo(self):
        return self.subgrupo
    
    def set_subgrupo(self, subgrupo):
        self.subgrupo = subgrupo

    def get_tipo_material(self):
        return self.tipo_material
    
    def set_tipo_material(self, tipo_material):
        self.tipo_material = tipo_material

    def get_classificacao_item(self):
        return self.classificacao_item
    
    def set_classificacao_item(self, classificacao_item):
        self.classificacao_item = classificacao_item

    def get_classificacao_anvisa(self):
        return self.classificacao_anvisa
    
    def set_classificacao_anvisa(self, classificacao_anvisa):
        self.classificacao_anvisa = classificacao_anvisa

    def get_ultima_entrada(self):
        return self.ultima_entrada
    
    def set_ultima_entrada(self, ultima_entrada):
        self.ultima_entrada = ultima_entrada

    def get_ultima_saida(self):
        return self.ultima_saida
    
    def set_ultima_saida(self, ultima_saida):
        self.ultima_saida = ultima_saida
    
    def get_vl_item(self):
        return self.vl_item
    
    def set_vl_item(self, vl_item):
        self.vl_item = vl_item
    
    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_dias_s_movto(self):
        return self.dias_s_movto
    
    def set_dias_s_movto(self, dias_s_movto):
        self.dias_s_movto = dias_s_movto