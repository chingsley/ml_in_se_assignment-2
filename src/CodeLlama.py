import replicate
import os


REPLICATE_API_TOKEN = os.environ["REPLICATE_API_TOKEN"]


class CodeLlama:

    def __init__(self):
        self.client = replicate.Client(api_token=REPLICATE_API_TOKEN)

    def prompt(self, prompt):
        output = self.client.run(
            "lucataco/orpheus-3b-0.1-ft:79f2a473e6a9720716a473d9b2f2951437dbf91dc02ccb7079fb3d89b881207f",
            input={"prompt": prompt},
        )
        return "".join(output)
