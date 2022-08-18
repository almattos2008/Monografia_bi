import domain.usecase.IdentifierUseCase as iuc


class IdentifyRoute:

    def __init__(self):
        self.identifier_uc = iuc.IdentifierUseCase()

    def identify(self):
        self.identifier_uc.identifify_english()
        # self.identifier_uc.identify()

ir = IdentifyRoute()
ir.identify()
