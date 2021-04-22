from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class ClientViewSet(viewsets.ViewSet):
    AUTHORIZED_PARAMS = ['id', 'email', 'telefone']

    def list(self, request):
        # /api/clientes
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def create(self, request):
        # /api/clientes
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, queryparams=None):
        # /api/clientes/<str:id>
        if queryparams.isdigit():
            cliente = self.__get_by_id(queryparams)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data)
        else:
            queries = queryparams.split('&')
            print(queries)

            if len(queries) == 1:
                param, value = queries[0].split('=')

                if param in self.AUTHORIZED_PARAMS:
                    if param == 'id':
                        cliente = self.__get_by_id(value)
                    elif param == 'email':
                        cliente = self.__get_by_email(value)
                    else:
                        cliente = self.__get_by_telefone(value)
                    
                    serializer = ClienteSerializer(cliente)
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, id=None):
        # /api/clientes/<str:id>
        cliente = Cliente.objects.get(id=id)
        serializer = ClienteSerializer(instance=cliente, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, id=None):
        # /api/clientes/<str:id>
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def __get_by_id(self, id=None):
        return Cliente.objects.get(id=id)
    
    def __get_by_email(self, email=None):
        try:
            email = Email.objects.raw('SELECT * FROM client_email WHERE email = %s', [email])[0]
            cliente = Cliente.objects.raw('SELECT * FROM client_cliente WHERE email_id = %s', [email.id])[0]
            
            return cliente
        except:
            return None

    def __get_by_telefone(self, telefone=None):
        try:
            telefone = Email.objects.raw('SELECT * FROM client_telefone WHERE numero = %s', [telefone])[0]
            cliente = Cliente.objects.raw('SELECT * FROM client_cliente WHERE telefone_id = %s', [telefone.id])[0]
            
            return cliente
        except:
            return None

class TelefoneViewSet(viewsets.ViewSet):
    def list(self, request):
        # /api/telefones
        telefones = Telefone.objects.all()
        serializer = TelefoneSerializer(telefones, many=True)
        return Response(serializer.data)

    def create(self, request):
        # /api/telefones
        serializer = TelefoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, id=None):
        # /api/telefones/<str:id>
        telefone = Telefone.objects.get(id=id)
        serializer = TelefoneSerializer(telefone)
        return Response(serializer.data)

    def update(self, request, id=None):
        # /api/telefones/<str:id>
        telefone = Telefone.objects.get(id=id)
        serializer = TelefoneSerializer(instance=telefone, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, id=None):
        # /api/telefones/<str:id>
        telefone = Telefone.objects.get(id=id)
        telefone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmailViewSet(viewsets.ViewSet):
    def list(self, request):
        # /api/emails
        emails = Email.objects.all()
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data)

    def create(self, request):
        # /api/emails
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, id=None):
        # /api/emails/<str:id>
        email = Email.objects.get(id=id)
        serializer = EmailSerializer(email)
        return Response(serializer.data)

    def update(self, request, id=None):
        # /api/emails/<str:id>
        email = Email.objects.get(id=id)
        serializer = EmailSerializer(instance=email, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, id=None):
        # /api/emails/<str:id>
        email = Email.objects.get(id=id)
        email.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
