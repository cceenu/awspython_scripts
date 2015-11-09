import boto3
li =[]
ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values' : ['stopped']}])
print instances
for instance in instances : 
	print(instance.id, instance.instance_type)
	li.append(instance.id)
	
ec2.instances.filter(InstanceIds=li).start()
