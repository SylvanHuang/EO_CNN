#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 01:18, 29/03/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieunguyen5991                                                  %
#-------------------------------------------------------------------------------------------------------%

from models.root.hybrid.root_hybrid_elm import RootHybridElm
from mealpy.evolutionary_based import GA, DE


class GaElm(RootHybridElm):
    def __init__(self, root_base_paras=None, root_hybrid_paras=None, ga_paras=None):
        RootHybridElm.__init__(self, root_base_paras, root_hybrid_paras)
        self.epoch = ga_paras["epoch"]
        self.pop_size = ga_paras["pop_size"]
        self.pc = ga_paras["pc"]
        self.pm = ga_paras["pm"]
        self.filename = "GA_ELM-" + root_hybrid_paras["paras_name"]

    def _training__(self):
        ga = GA.BaseGA(self._objective_function__, self.problem_size, self.domain_range, self.log, self.epoch, self.pop_size, self.pc, self.pm)
        self.solution, self.best_fit, self.loss_train = ga._train__()


class DeElm(RootHybridElm):
    def __init__(self, root_base_paras=None, root_hybrid_paras=None, de_paras=None):
        RootHybridElm.__init__(self, root_base_paras, root_hybrid_paras)
        self.epoch = de_paras["epoch"]
        self.pop_size = de_paras["pop_size"]
        self.wf = de_paras["wf"]
        self.cr = de_paras["cr"]
        self.filename = "DE_ELM-" + root_hybrid_paras["paras_name"]

    def _training__(self):
        de = DE.BaseDE(self._objective_function__, self.problem_size, self.domain_range, self.log, self.epoch, self.pop_size, self.wf, self.cr)
        self.solution, self.best_fit, self.loss_train = de._train__()
