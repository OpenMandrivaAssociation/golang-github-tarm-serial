# Run tests in check section
%bcond_without check

%global goipath         github.com/tarm/serial
%global commit          eaafced92e9619f03c72527efeab21e326f3bc36

%global common_description %{expand:
A Go package to allow you to read and write from the serial port as a 
stream of bytes.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Read and write from the serial port as a stream of bytes
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/sys/unix)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.giteaafced
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180417giteaafced
- First package for Fedora

