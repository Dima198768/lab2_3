import zeep

wsdl = 'http://localhost:8000/?wsdl'
client = zeep.Client(wsdl=wsdl)

#echo SOAP
echoText = input("Enter echo text: ")
print(client.service.echo(echoText))
