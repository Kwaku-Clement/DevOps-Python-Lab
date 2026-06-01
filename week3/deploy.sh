#!/bin/bash

DEPLOY_DIR="$HOME/deployments/myapp"
echo "Starting deployment setup..."
mkdir -p "$DEPLOY_DIR"/{logs,config,bin}

if [ -f "analyze_log.sh" ]; then
    cp analyze_log.sh "$DEPLOY_DIR"/bin/
    chmod +x "$DEPLOY_DIR"/bin/analyze_log.sh
    echo "Successfully copied analyze_log.sh to $DEPLOY_DIR/bin/."
else
    echo "Warning: analyze_log.sh not found in current directory to copy."
fi

echo "Deployment setup completed at: $DEPLOY_DIR."
