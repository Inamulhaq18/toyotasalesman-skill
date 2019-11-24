from mycroft import MycroftSkill, intent_file_handler


class Toyotasalesman(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('toyotasalesman.intent')
    def handle_toyotasalesman(self, message):
        self.speak_dialog('toyotasalesman')


def create_skill():
    return Toyotasalesman()

