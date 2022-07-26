from cloudify import ctx
from cloudify.state import ctx_parameters as p


public_ip_address = ctx.instance.runtime_properties.get('resources', {}).get(
    'eip','fip').get('instances',[])[0].get('attributes',{}).get('public_ip')

ctx.instance.runtime_properties['public_ip_address'] = public_ip_address
