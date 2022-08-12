import domain.usecase.IdentifierUseCase as iuc


class IdentifyRoute:

    def __init__(self):
        self.identifier_uc = iuc.IdentifierUseCase()

    def identify(self):
        self.identifier_uc.identifify_xlm_roberta_large_model()

ir = IdentifyRoute()
ir.identify()
