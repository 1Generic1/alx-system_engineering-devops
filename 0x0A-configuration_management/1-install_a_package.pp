#!/usr/bin/pup
# Puppet manifest to install Flask with version 2.1.0
# Install Flask with version 2.1.0
package { 'flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3',
}
