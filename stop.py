import boto3
ec2 = boto3.resource('ec2')
li = []
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values' : ['running']}])
for instance in instances :
	li.append(instance.id)

ec2.instances.filter(InstanceIds=li).stop()	
