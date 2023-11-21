from django.db import models
from django.conf import settings
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(BaseModel):
    author = models.ForeignKey("users.Author", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    summarized_content = models.TextField(null=True, blank=True)

    def summarize_note_using_langchain(self):
        txt = str(self.content)
        llm = OpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY)
        text_splitter = CharacterTextSplitter()
        texts = text_splitter.split_text(txt)
        docs = [Document(page_content=t) for t in texts]
        chain = load_summarize_chain(llm, chain_type='map_reduce')
        self.summarized_content = chain.run(docs)
        self.save(update_fields=['summarized_content', 'updated'])
