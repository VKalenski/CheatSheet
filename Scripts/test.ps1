# Chocolatey
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Output "Chocolatey it is not installed. Installation..."
    
    # Install Chocolatey
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor  [System.Net.SecurityProtocolType]::Tls12;
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    
    Write-Output "Chocolatey беше успешно инсталиран."
} else {
    Write-Output "Chocolatey is already installed."
}

# Docker Installation
$dockerInstalled = choco list --local-only | Select-String docker

if ($dockerInstalled) {
    Write-Output "Docker is installed already."
} else {
    Write-Output "Docker it is not installed. Installation..."
    
    # Install Docker
    choco install docker-desktop -y
    
    Write-Output "Docker is installed."
}

# Check Docker version
docker --version
