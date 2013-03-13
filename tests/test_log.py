import os
import sys

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                                os.pardir,
                                                os.pardir))
if os.path.exists(os.path.join(possible_topdir, 'alerta', '__init__.py')):
    sys.path.insert(0, possible_topdir)

from alerta.common import log as logging
from alerta.common import config

LOG = logging.getLogger('alerta.ircbot')
CONF = config.CONF

if __name__ == '__main__':
    config.parse_args(sys.argv[1:])
    logging.setup('alerta')

    LOG.fatal('test fatal')
    LOG.critical('test critical')
    LOG.error('test error')
    LOG.warn('test warn')
    LOG.warning('test warning')
    LOG.info('test info')
    LOG.debug('test debug')

