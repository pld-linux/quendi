Summary:	electronics conversations
Summary(pl):	elektroniczne konwersacje
Name:		quendi
Version:	1.0.2
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://aleph-0.dhs.org/people/loth/%{name}-%{version}.tar.gz
# Source0-md5:	5a6b5daaed703cead74a22089f1c5c55
Patch0:		%{name}-types.patch
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quendi is ideology, but you can treat it like a game. That is useful
to have a conversations with androids and make electronics people. :)

%description -l pl
Projekt pokazuj±cy ¿e grafika nie jest czym¶ koniecznym. Ideologiczna
rozmowa z androidem przeklête tworzenie elektronicznych postaci w
krainie ia. Nic specjalnego je¿eli traktujesz to jak grê.

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
